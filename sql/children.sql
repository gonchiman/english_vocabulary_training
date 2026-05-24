create table if not exists children (
    word text not null,
    parent text not null,
    primary key (word, parent),
    foreign key (word) references parents(word) on delete cascade
);