/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     27/08/2021 2:57:15 p. m.                     */
/*==============================================================*/


drop index RELATIONSHIP_5_FK;

drop index RELATIONSHIP_2_FK;

drop index CHARACTERS_PK;

drop table CHARACTERS;

drop index CITY_PK;

drop table CITY;

drop index POWERS_PK;

drop table POWERS;

drop index RELATIONSHIP_4_FK;

drop index RELATIONSHIP_3_FK;

drop index POWERS_CHARACTER_PK;

drop table POWERS_CHARACTER;

drop index UNIVERSES_PK;

drop table UNIVERSES;

/*==============================================================*/
/* Table: CHARACTERS                                            */
/*==============================================================*/
create table CHARACTERS (
   ID                   SERIAL               not null,
   CIT_ID               INT4                 null,
   UNI_ID               INT4                 null,
   NAME                 VARCHAR(200)         null,
   PATH                 VARCHAR(200)         null,
   DESCRIPTION          VARCHAR(500)         null,
   constraint PK_CHARACTERS primary key (ID)
);

/*==============================================================*/
/* Index: CHARACTERS_PK                                         */
/*==============================================================*/
create unique index CHARACTERS_PK on CHARACTERS (
ID
);

/*==============================================================*/
/* Index: RELATIONSHIP_2_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_2_FK on CHARACTERS (
CIT_ID
);

/*==============================================================*/
/* Index: RELATIONSHIP_5_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_5_FK on CHARACTERS (
UNI_ID
);

/*==============================================================*/
/* Table: CITY                                                  */
/*==============================================================*/
create table CITY (
   ID                   SERIAL               not null,
   NAME                 VARCHAR(200)         null,
   LAT                  FLOAT8         null,
   LON                  FLOAT8         null,
   constraint PK_CITY primary key (ID)
);

/*==============================================================*/
/* Index: CITY_PK                                               */
/*==============================================================*/
create unique index CITY_PK on CITY (
ID
);

/*==============================================================*/
/* Table: POWERS                                                */
/*==============================================================*/
create table POWERS (
   ID                   SERIAL               not null,
   NAME                 VARCHAR(200)         null,
   constraint PK_POWERS primary key (ID)
);

/*==============================================================*/
/* Index: POWERS_PK                                             */
/*==============================================================*/
create unique index POWERS_PK on POWERS (
ID
);

/*==============================================================*/
/* Table: POWERS_CHARACTER                                      */
/*==============================================================*/
create table POWERS_CHARACTER (
   ID                   SERIAL               not null,
   POW_ID               INT4                 null,
   CHA_ID               INT4                 null,
   LEVEL                FLOAT8               null,
   constraint PK_POWERS_CHARACTER primary key (ID)
);

/*==============================================================*/
/* Index: POWERS_CHARACTER_PK                                   */
/*==============================================================*/
create unique index POWERS_CHARACTER_PK on POWERS_CHARACTER (
ID
);

/*==============================================================*/
/* Index: RELATIONSHIP_3_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_3_FK on POWERS_CHARACTER (
POW_ID
);

/*==============================================================*/
/* Index: RELATIONSHIP_4_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_4_FK on POWERS_CHARACTER (
CHA_ID
);

/*==============================================================*/
/* Table: UNIVERSES                                             */
/*==============================================================*/
create table UNIVERSES (
   ID                   SERIAL               not null,
   NAME                 VARCHAR(100)         null,
   DESCRIPTION          VARCHAR(400)         null,
   FOUNDATION           DATE                 null,
   constraint PK_UNIVERSES primary key (ID)
);

/*==============================================================*/
/* Index: UNIVERSES_PK                                          */
/*==============================================================*/
create unique index UNIVERSES_PK on UNIVERSES (
ID
);

alter table CHARACTERS
   add constraint FK_CHARACTE_RELATIONS_CITY foreign key (CIT_ID)
      references CITY (ID)
      on delete restrict on update restrict;

alter table CHARACTERS
   add constraint FK_CHARACTE_RELATIONS_UNIVERSE foreign key (UNI_ID)
      references UNIVERSES (ID)
      on delete restrict on update restrict;

alter table POWERS_CHARACTER
   add constraint FK_POWERS_C_RELATIONS_POWERS foreign key (POW_ID)
      references POWERS (ID)
      on delete restrict on update restrict;

alter table POWERS_CHARACTER
   add constraint FK_POWERS_C_RELATIONS_CHARACTE foreign key (CHA_ID)
      references CHARACTERS (ID)
      on delete restrict on update restrict;
