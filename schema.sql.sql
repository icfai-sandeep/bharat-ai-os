-- BharatAI Users Table
create table if not exists users (
  id text primary key,
  name text,
  credits int default 3,
  streak int default 0,
  user_type text default 'mixed',
  chat_history jsonb default '[]'::jsonb,
  created_at timestamp with time zone default now()
);