create table if not exists quiz_records (
    word text not null,
    date text not null,
    children_count integer not null,
    correct_count integer not null,
    primary key (word, date),
    foreign key (word) references parents(word) on delete cascade
);