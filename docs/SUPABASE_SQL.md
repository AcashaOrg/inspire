# Supabase SQL Setup

This document provides example SQL commands to create the core tables for the Synergy Tutor pilot on Supabase. The commands assume that Supabase Auth is used and `auth.uid()` returns the SSO identifier for the current user.

## Enable extensions
```sql
create extension if not exists "pgcrypto";
```

## Reference tables
```sql
-- Students and teachers, typically populated via SSO
create table if not exists students (
  id text primary key,
  full_name text
);

create table if not exists teachers (
  id text primary key,
  full_name text
);

create table if not exists classes (
  id uuid primary key default gen_random_uuid(),
  class_name text not null
);

create table if not exists class_enrollments (
  class_id uuid references classes(id) on delete cascade,
  student_id text references students(id) on delete cascade,
  primary key (class_id, student_id)
);

create table if not exists teacher_class_assignments (
  class_id uuid references classes(id) on delete cascade,
  teacher_id text references teachers(id) on delete cascade,
  primary key (class_id, teacher_id)
);
```

## `StudentChats` table
```sql
create table if not exists student_chats (
  id uuid primary key default gen_random_uuid(),
  student_id text not null references students(id),
  session_id uuid not null,
  timestamp timestamptz not null default now(),
  actor text not null,
  message_text text,
  original_message_text text,
  token_count integer,
  reading_level numeric,
  topic_code text,
  other_analytics_tags jsonb
);

create index if not exists idx_student_chats_student_session on student_chats (student_id, session_id);
create index if not exists idx_student_chats_session_timestamp on student_chats (session_id, timestamp);
```

## `TeacherNotes` table
```sql
create table if not exists teacher_notes (
  note_id uuid primary key default gen_random_uuid(),
  teacher_id text not null references teachers(id),
  student_id text references students(id),
  session_id uuid references student_chats(session_id),
  timestamp timestamptz not null default now(),
  note_text text not null
);

create index if not exists idx_teacher_notes_teacher on teacher_notes (teacher_id);
create index if not exists idx_teacher_notes_student on teacher_notes (student_id);
```

## Row-Level Security (RLS)
```sql
-- Enable RLS on the two main tables
alter table student_chats enable row level security;
alter table teacher_notes enable row level security;
```

### Policies for `student_chats`
```sql
-- Students can insert and read their own chats
create policy "Students manage own chats" on student_chats
  for all using (auth.uid() = student_id);

-- Teachers can read chats for students in their classes
create policy "Teachers can view class chats" on student_chats
  for select using (
    exists (
      select 1
      from class_enrollments ce
      join teacher_class_assignments tca on ce.class_id = tca.class_id
      where ce.student_id = student_chats.student_id
        and tca.teacher_id = auth.uid()
    )
  );
```

### Policies for `teacher_notes`
```sql
-- Teachers can create and edit their own notes
create policy "Teachers manage own notes" on teacher_notes
  for all using (auth.uid() = teacher_id);
```
