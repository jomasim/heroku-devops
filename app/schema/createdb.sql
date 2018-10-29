create table if not exists users(
    id serial not null primary key,
    name varchar not null,
    username varchar not null,
    email varchar not null,
    role varchar not null,
    password varchar not null,
    create_at timestamp not null default now(),
    updated_at timestamp default current_timestamp
);

create table if not exists products(
    id serial not null primary key,
    name varchar not null,
    category varchar not null,
    price varchar not null,
    description text not null,
    created_by integer not null references users(id),
    create_at timestamp not null default now(),
    updated_at timestamp default current_timestamp
);

create table if not exists sales(
    id serial not null primary key,
    line_items text not null,
    created_by integer not null references users(id),
    create_at timestamp not null default now(),
    updated_at timestamp default current_timestamp
);