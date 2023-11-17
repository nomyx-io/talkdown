---
title: Technical content creator
---

This process creates technical content for an Astro Starlight website.

## Process Flowchart

flowchart TB
    start("Start") --> codebaseAnalysis[01_codebase_analysis]
    codebaseAnalysis --> commentExtraction
    codebaseAnalysis --> apiDocumentation
    codebaseAnalysis --> codeExampleGeneration

    commentExtraction[02_comment_extraction_interpretation] --> markdownConversion
    apiDocumentation[03_api_docummentation] --> markdownConversion
    codeExampleGeneration[04_code_example_generation] --> markdownConversion

    markdownConversion[05_markdown_conversion] --> navigationStructure
    markdownConversion --> versionControlDoc

    navigationStructure[06_navigation_structure] --> astroIntegration
    versionControlDoc[07_version_control] --> astroIntegration

    astroIntegration[08_astro_integration] --> starlightFeatures
    astroIntegration --> accessibilitySeoOptimization

    starlightFeatures[09_starlight_feature_highlighting] --> automatedPublishing
    accessibilitySeoOptimization[10_accessibility_seo_optimization] --> automatedPublishing

    automatedPublishing[11_automated_publishing] --> feedbackLoop
    feedbackLoop[12_feedback_loop] --> |"13_documentation_update"| codebaseAnalysis

    feedbackLoop[End]

## Directives to create technical content

### Codebase Analysis Directive

Analyzes a codebase to identify structures, patterns, functions, and classes that require documentation.

### Comment Extraction and Interpretation Directive

Extracts and interprets inline comments from the codebase, turning them into comprehensive explanations and descriptions.

### API Documentation Directive

Automatically generates documentation for public APIs, including method signatures, parameters, returns, and sample code snippets.

### Code Example Generation Directive

Creates accurate and relevant code examples that demonstrate the use of functions, classes, or interfaces within the codebase.

### Markdown Conversion Directive

Converts analysis and commentary into structured Markdown files ready for website integration.

### Navigation Structure Directive

Determines the optimal structure for navigation and content organization within the documentation website.

### Astro Integration Directive

Seamlessly integrates the generated Markdown into Astro projects to prepare for static site generation.

### Starlight Feature Highlighting Directive

Identifies and accentuates the features and capabilities of the Starlight tool within the generated documentation.

### Version Control Documentation Directive

Tracks differences between codebase versions and updates the documentation to reflect changes across versions.

### Accessibility and SEO Optimization Directive

Ensures that the generated documentation is accessible, and optimizes it for search engines to improve findability.

### Automated Publishing Directive

Automates the process of deploying the updated static site whenever changes to documentation are made.

### Feedback Loop Directive

Implements a feedback system for users to suggest improvements or report issues with the documentation, which feeds into the iterative documentation update process.

### Documentation Update Directive

Updates the documentation based on user feedback, codebase changes, and new features.

## Implementation

The directives all need to be implemented and saved to the `docwriter` directory in the Astro codebase. The directives should be implemented in the following order:

1. Codebase Analysis
2. Comment Extraction and Interpretation
3. API Documentation
4. Code Example Generation
5. Markdown Conversion
6. Navigation Structure
7. Astro Integration
8. Starlight Feature Highlighting
9. Version Control Documentation
10. Accessibility and SEO Optimization
11. Automated Publishing
12. Feedback Loop
13. Documentation Update

Once the directives are created, this section ('Implementation') and its content should be removed from this document, and a new section should be added in its place, titled 'Execution'. The 'Execution' section should contain the following information:

* The name of the directive
* A link to the directive
