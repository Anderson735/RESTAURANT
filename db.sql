create schema trabajo_arle;
use trabajo_arle;

create table eventos
( 
  id_evento char(20) primary key not null,
  fecha_publicacion date,
  Descripcion varchar(250),
  id_restaurante char(20),
  fecha_evento date,
  fecha_final date,
  estado_evento char(1)
);

create table restaurante
(
	id_restaurante char(20) primary key not null,
    nombre varchar(100),
    direccion varchar(100),
    telefono char(20),
    categoria char(50)
);

alter table eventos add foreign key(id_restaurante)
references restaurante(id_restaurante);