# Textbook Formatting Guide 
This is the formatting guide for working on the textbook. This is to make sure that the LaTeX file stays clean and that there is a consistent format for the textbook across multiple authors.

## Textbook organization
### Chapters
Chapters are the top level and should have a short succinct title. Each chapter should cover a distinct concept and should be readable in a self-contained manner.

### Section
Sections are the next degree of division within a chapter. Each section should be a sensible division of the content within a chapter, and each chapter should have at most 4-5 sections. Sections should be numbered, and should be created using the command
```
\section{NAME}
```

### Subsection
Subsections should delineate individual portions within a given section. For example, you might have a subsection for setting up a model, another for solving the model, and another for the conclusions of the model. However, to avoid cluttering the table of contents, subsections should not be explicitly numbered, and so should be created using the command
```
\subsection*{NAME}
```

### Environments
All environments should be unnumbered by default. So instead of using
```
\begin{theorem}
\end{theorem}
```
Prefer instead,
```
\begin{theorem*}
\end{theorem*}
```


## References
### Labels
To label a section, equation, theorem, etc., use the following naming conventions:
* Chapter `\label{ch:LABEL}`
* Section `\label{sec:LABEL}`
* Theorem `\label{thm:LABEL}`
* Equation `\label{eq:LABEL}`

### Referring
To create a reference to a given label, use `\ref{LABEL}`. You should write what the reference is to in the text though, so instead of writing
```
This is shown in \ref{sec:example_section}
```
It should instead be written as
```
This is shown in section \ref{sec:example_section}
```

### Numbered vs unnumbered environments
In general, an environment without an asterisk will be numbered by default and an environment with an asterisk will be unnumbered. Here is a breakdown of what should and should not be numbered vs unnumbered.

#### Numbered

#### Unnumbered
* Align


## Text style
### Capitalization
All chapter names, sections, and subsections should be in "title case." So capitalize all words except for common articles, conjunctions, etc. 

## Plots
For function plots, use Mathematica to generate the plots. Plots should also be centered in the page if on a line by themselves, and accompanied by a brief caption describing the plot. 