# Gemini Project Context: Personal Portfolio Website

This file provides context for interacting with the personal portfolio project of Joseph Rey C. Marilla.

## Project Overview

This is a personal portfolio website hosted on GitHub Pages. It showcases Joseph Rey C. Marilla's professional experience, skills, and projects as an IT Operations Specialist. The project is designed to be flexible, supporting multiple interchangeable HTML5 UP themes.

Currently, the project contains two main themes:
*   **Original Theme:** A portfolio theme based on HTML5 UP's Hyperspace. Its files are located in the project's root.
*   **Dimension Theme:** An alternative theme based on HTML5 UP's Dimension, which has been customized to include the portfolio content. Its files are located in the `html5up-dimension/` subfolder.

The `_config.yml` file specifies a `baseurl` of `/MyProfile`, which is relevant for GitHub Pages deployment.

## Building and Running

This is a static HTML website. No build process is required.

*   **To view the currently active theme:** Open the root `index.html` file in a web browser.
*   **To preview a specific theme:** Open the `index.html` file located within that theme's subfolder (e.g., `html5up-dimension/index.html`).

## Development Conventions

### Theme Management

The primary development convention is the management of multiple themes. Each theme should be self-contained in its own directory (e.g., `original-theme/`, `html5up-dimension/`).

To make a theme live on GitHub Pages, its entire contents (including `index.html`, `assets/`, `images/`, etc.) must be copied to the root of the repository before committing and pushing.

**Note on Pushing:** The `git push` command will sync your entire local repository with GitHub, including all theme subfolders. This ensures that all theme options are always available in your remote repository, and you won't lose any themes when switching between machines.

A detailed guide for this process is available in `theme_interchange_guide.txt`.

### Key Files

*   `index.html`: The main entry point for the currently active theme (when in the root directory).
*   `html5up-dimension/`: A subfolder containing all files for the "Dimension" theme.
*   `theme_interchange_guide.txt`: A step-by-step guide on how to switch between available themes for deployment on GitHub Pages.
*   `assets/`: Contains the CSS, JavaScript, and SASS files for the currently active theme.
*   `images/`: Contains image assets for the currently active theme.
*   `_config.yml`: Jekyll configuration file for GitHub Pages.
*   `.nojekyll`: A file that disables Jekyll processing on GitHub Pages, ensuring that static files are served as-is.
*   `package.json`: Contains basic project metadata but no scripts or dependencies, suggesting it might be for informational purposes or future development.

**TODO:** The original theme files in the root should be moved into their own `original-theme/` subfolder to streamline the theme-switching process, as detailed in `theme_interchange_guide.txt`.
