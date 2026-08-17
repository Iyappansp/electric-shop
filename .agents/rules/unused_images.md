# Unused Image Management Rule

When auditing and managing website assets across projects:

1. **Identification**:
   - Scan all image files (`.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg`, `.ico`, `.avif`).
   - Check references against all source files (`.html`, `.css`, `.js`, `.json`, `.py`, `.md`).
   - Images not referenced in any source files are flagged as unused.

2. **Isolation (`unused/` folder)**:
   - Move unused images into a dedicated `unused/` directory at the project root.
   - Preserve original relative subfolder structure (e.g. `unused/assets/cta/image.png`) to avoid filename collisions and retain file origin context.
   - Never alter website source code (.html, .css, .js) when isolating unused images.

3. **Safe Deletion Policy**:
   - Keep images in `unused/` for verification before permanent deletion.
