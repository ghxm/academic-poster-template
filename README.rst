This is a fork of cpitclaudel's ``academic-poster-template``.

Run ``./render.py custom_poster_template.jinja2 output.html`` to render the poster.

The templates folder contains the modified original template used as a base for ``my_poster.jinja2``.

## Usage

   ``
   ./render.py my_poster.jinja2 output.html --bibtex library.bib
   ``

See original ``README.rst`` below.

-----

==========================================================
 A template for (more) accessible posters, using HTML+CSS
==========================================================

Modern HTML+CSS is more than enough for most academic posters:

- No more fighting with LaTeX+Beamer or PowerPoint/LibreOffice.
- It works on computers, tablets, and mobile devices.
- Readers can adjust the font size trivially.
- It's much more accessible than PDFs.

.. image:: docs/tutorial/logo.svg
   :align: center

See it in action `on a real example <https://cpitclaudel.github.io/academic-poster-template/koika/poster.html>`__ and `follow the tutorial <https://cpitclaudel.github.io/academic-poster-template/tutorial/poster.html>`__ to create your own posters.
