# fraudat

## Instalación de nvm (Node Version Manager)

`nvm` es una herramienta que permite instalar y cambiar entre diferentes versiones de Node.js fácilmente.

### Instalación de nvm

1. Descarga e instala `nvm` siguiendo las instrucciones para tu sistema operativo desde el [repositorio oficial de nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

2. [NVM for Windows](https://github.com/coreybutler/nvm-windows).

### Instalación de una versión específica de Node.js

Para instalar una versión específica de Node.js, usa el siguiente comando:

```sh
nvm install <version>
```

Por ejemplo, para instalar la versión 14.17.0:

```sh
nvm install 14.17.0
```

### Listar versiones instaladas de Node.js

Para listar todas las versiones de Node.js instaladas en tu sistema, usa:

```sh
nvm ls
```

### Cambiar la versión de Node.js

Para cambiar a una versión específica de Node.js que ya has instalado, usa:

```sh
nvm use <version>
```

Por ejemplo, para cambiar a la versión 14.17.0:

```sh
nvm use 14.17.0
```

### Listar versiones disponibles para instalar

Para listar todas las versiones de Node.js disponibles para instalar, usa:

```sh
nvm ls-remote
```

### Establecer una versión predeterminada de Node.js

Para establecer una versión predeterminada de Node.js que se usará en nuevas sesiones de terminal, usa:

```sh
nvm alias default <version>
```

Por ejemplo, para establecer la versión 14.17.0 como predeterminada:

```sh
nvm alias default 14.17.0
```