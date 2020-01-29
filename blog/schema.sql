drop table if exists post;

create table post (
    id integer primary key autoincrement,
    title varchar(120) not null,
    body text not null,
    create_at timestamp not null default current_timestamp,
    autho varchar(32)
)