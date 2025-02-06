# Convenciones para mensajes de commits (Changelog)

Los mensajes de commit deben ser claros y seguir una estructura consistente para facilitar la lectura y el mantenimiento del historial de cambios. Utilizamos las siguientes convenciones:

### Tipos de Commit
- **`feat`**: Para nuevas características o funcionalidades.  
  *Ejemplo: `feat: add user authentication module`*  
- **`fix`**: Para correcciones de errores.  
  *Ejemplo: `fix: resolve null pointer exception in login service`*  
- **`docs`**: Para cambios en la documentación.  
  *Ejemplo: `docs: update API usage examples in README.md`*  
- **`style`**: Para cambios que no afectan la lógica del código (formato, punto y coma, espacios en blanco, etc.).  
  *Ejemplo: `style: format code according to ESLint rules`*  
- **`refactor`**: Para refactorizaciones que mejoran el código sin cambiar su funcionalidad o corregir errores.  
  *Ejemplo: `refactor: simplify user service logic`*  
- **`test`**: Para añadir o modificar pruebas.  
  *Ejemplo: `test: add unit tests for authentication controller`*  
- **`perf`**: Para mejoras en el rendimiento.  
  *Ejemplo: `perf: optimize database queries in transaction module`*  
- **`build`**: Para cambios en la configuración del build o herramientas externas.  
  *Ejemplo: `build: update webpack configuration to support code splitting`*  
- **`ci`**: Para cambios en la configuración o scripts de integración continua.  
  *Ejemplo: `ci: add GitHub Actions workflow for automated testing`*  
- **`remove`**: Para indicar la eliminación de un archivo, módulo o funcionalidad.  
  *Ejemplo: `remove: delete unused legacy code`*  
- **`chore`**: Para tareas de mantenimiento que no afectan el código fuente.  
  *Ejemplo: `chore: update project dependencies to latest versions`*  
- **`revert`**: Para revertir un commit anterior.  
  *Ejemplo: `revert: undo changes introduced in commit abc123`*

---

## Reglas Generales para Commits
1. **Escribir en presente imperativo**: Describe qué hace el cambio, no qué hizo.  
   *Ejemplo: `add feature` en lugar de `added feature`.*
2. **Brevedad y claridad**: El título debe ser corto, aproximadamente **50 caracteres**.  
3. **Detalles adicionales (opcional)**: Si el cambio es complejo, agrega una descripción detallada en un párrafo separado.  
4. **Referencias a issues**: Si corresponde, incluye referencias al issue o ticket relacionado (e.g., `fix: resolve login bug (#123)`).

---

## Ejemplos de Commits
```bash
git commit -m "feat: implement user registration endpoint"
git commit -m "fix: correct typo in email validation"
git commit -m "style: adjust indentation in main.css"
git commit -m "test: add integration tests for payment gateway"
git commit -m "chore: bump Node.js version in Dockerfile"
```

## Comando para agregar todos los commits al changelog.
```bash
git log --pretty=format:"## %h - %s%nAuthor: %an%nDate: %ad%n%n" --date=short > CHANGELOG.md
```

# Etiquetas para Issues en GitHub
- **bug**: Algo no está funcionando.  
- **documentation**: Mejoras o adiciones a la documentación.  
- **duplicate**: Este issue o pull request ya existe.  
- **enhancement**: Nueva característica o solicitud.  
- **good first issue**: Bueno para principiantes.  
- **help wanted**: Se necesita atención adicional.  
- **invalid**: Esto no parece correcto.  
- **question**: Se solicita más información.  
- **wontfix**: Esto no se trabajará.  