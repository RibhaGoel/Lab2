---
name: Lab2 Project Instructions
description: Guidelines for developing the educational assignment portal website
---

# Lab2 - Educational Assignment Portal

## Project Overview

This is an educational website for sharing homework assignments and coding exercises with students. Students can browse, view, and download assignments directly from the portal.

## Project Structure & Organization

### Core Directories
- **`assignments/`** - Each homework assignment stored in its own subfolder with consistent structure
- **`templates/`** - Reusable templates for new content
- **`assets/`** - Website assets (CSS, JavaScript, images, configuration)
- **`index.html`** - Main portal page serving as the browsing interface
- **`config.json`** - Dynamic configuration for assignment lists and details

### Naming Conventions
- Use descriptive, lowercase names for files and folders
- Use hyphens to separate words in filenames (e.g., `assignment-template.md`, `starter-code.py`)
- Keep folder structures flat and organized by assignment type

## Development Guidelines

### Code Quality
- Maintain consistent styling across all pages and components
- Follow existing code patterns in the repository
- Ensure responsive design for mobile and desktop views

### Asset Management
- Place CSS files in `assets/css/`
- Place JavaScript files in `assets/js/`
- Place images in `assets/images/`
- Keep assets organized and avoid duplication

### HTML & Frontend
- Use semantic HTML markup
- Link CSS and JavaScript with relative paths
- Ensure all pages have consistent navigation and styling
- Test layout on multiple screen sizes

### Configuration
- Use `config.json` for dynamic content configuration
- Keep configuration structure predictable and maintainable
- Document any new configuration options

## Educational Standards

When generating or modifying content for this project:

### Learning-Focused Design
- Ensure all assignments have clear learning objectives
- Present content with appropriate difficulty levels
- Build concepts progressively across assignments
- Include explanatory comments in starter code

### Student-Friendly Approach
- Use clear, encouraging language
- Provide helpful comments and documentation
- Break complex tasks into manageable steps
- Include examples or reference materials when helpful
- Make error messages and feedback constructive

### Assignment Templates
- Follow the existing template structure in `templates/assignment-template.md`
- Include problem description, requirements, and starter code
- Provide clear submission instructions
- Document expected outcomes or success criteria

## Git & Version Control

- Use descriptive commit messages
- Keep commits focused on a single change or feature
- Test changes locally before committing
- Pull latest changes before starting new work

## Best Practices

- Before modifying configuration, understand how it affects the website
- When adding new assignments, follow existing folder structure conventions
- Keep documentation up-to-date with code changes
- Consider the student experience when designing new features
- Test assignment downloads and navigation flows
