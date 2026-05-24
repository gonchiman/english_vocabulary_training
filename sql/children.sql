create table if not exists children (
    word text not null,
    parent text not null,
    primary key (word, parent),
    foreign key (parent) references parents(word) on delete cascade
);