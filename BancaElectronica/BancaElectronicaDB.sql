create database BancaElectronica;
use BancaElectronica;
create table TIPO_EMPRESA(
IdEmpresa int primary key not null auto_increment,
Nombre varchar(50)
);
#creamos la tabla Empresa
#Rlegal = Representante Legal
create table EMPRESA(
NitEmpresa numeric(8,0) primary key not null,
NombreEmpresa varchar(50) not null,
NombreComercial varchar(50) not null,
RLegal varchar(75) not null,
Dirreccion varchar(250) not null,
TelefonoEmpresa numeric(8,0) not null,
TelefonoRLegal numeric(8,0) not null,
Email Varchar(50) not null,
TipoEmpresa int not null,
foreign key(TipoEmpresa) references TIPO_EMPRESA(IdEmpresa)
);
#drop database BancaElectronica; #eliminar Base de dato
#creando tabla Persona
create table PERSONA(
NitPersona numeric(8,0) primary Key not null,
CuiPersona numeric(13,0) not null,
Nombre varchar(50) not null,
Apellido varchar(50) not null,
FechaNacimiento date not null,
Telefono1 numeric(8,0) not null,
Telefono2 numeric(8,0) null,
Dirrecion varchar(250) not null,
Email varchar(50) not null
);
#Creando tabla Usuario para el Login
create table USUARIO(
IdUsuario int primary key not null auto_increment,
Usuario varchar(50) not null,
Contraseña varchar(50) not null,
TipoUsuario varchar(14) not null,
IngresosFallidos int not null
);
drop table CUENTA;
#Creando la tabla cuenta
create table CUENTA(
NoCuenta int(10) zerofill primary key not null auto_increment,
TipoCuenta varchar(10) not null,
Monto numeric(10,2) not null,
FechaApertura date not null,
Estado varchar(11) not null,
ClienteEmpresa numeric(8,0) null,
ClientePersona numeric(8,0) null,
#Cliente numeric(8,0) not null,
Usuario int null,
foreign key (ClienteEmpresa) references EMPRESA(NitEmpresa),
foreign key (ClientePersona) references PERSONA(NitPersona),
foreign key (Usuario) references USUARIO(IdUsuario)
);

