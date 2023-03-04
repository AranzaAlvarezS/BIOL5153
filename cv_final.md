---

name: Aranza
surname: Alvarez Sanabria
position: "Biological Sciences Graduate Assistant"
address: "Fayetteville, AR 72701"
phone: +1 (805) 263-9912
email: "aranza.alvarez.sanabria@gmail.com"
linkedin: Aranza Alvarez Sanabria
date: "`r format(Sys.time(), '%B %Y')`"
output: vitae::awesomecv
theme: fancy
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = FALSE, warning = FALSE, message = FALSE)
library(vitae)
```

# Skills


 * • Cell and Molecular Biology laboratory techniques: PCR, DNA cloning, Gel electrophoresis, arrays
 
 * • Data Analysis
 
 * • Specimen Collection and Testing
 
 * • Quality Assurance
 
 * • Analytical Thinking
 
 * • Research and Documentation
 
 * • Laboratory Safety Protocols
 
 * • Laboratory Maintenance

# Education

```{r}
library(tibble)
tribble(
  ~ Degree, ~ Year, ~ Institution, ~ Where,
 
  "BS Cell and Molecular Biology cum laude", "2018-22", "Seattle, WA", "Seattle University",
  "Master of Statistics and Analytics", "Expected 2025", "Fayetteville, AR", "University of Arkansas",
  
) %>% 
  detailed_entries(Degree, Year, Institution, Where)
```

# Work Experience

```{r}
library(tibble)
tribble(
  ~ Degree, ~ Year, ~ Institution, ~ Where,
 
    "• Facilitated laboratory coursework for two laboratory sections.
• Constructed and graded quizzes and exams for students.
• Utilized active learning startegies to teach new material to students.
• Assisted students with identifying anatomical structures throughout the body.
• Capacitated in laboratory safety and implemented lab procedures to prevent accidents.
", "2023-Current", "Teaching Assistant", "University of Arkansas",
  "• Analyzed disinfection and sanitization product samples using techniques like gas chromatography, Karl Fischer titration and spectrophotometry.
• Worked part time and analyzed samples for purity scores, density measurements and input findings in quality control documents for company inventory.
• Trusted to run tests independently outside use of extremely delicate instruments.
• Gained exposure to delicate procedures for quality control purposes.
• Implemented lab procedures to prevent errors and protect staff.", "Summer 2021", "Laboratory Assistant Internship at ARVI chemical Laboratories", "Cartago, Costa Rica",
  "• Analyzed quality of 80+ bovine embryos for embryo transfer procedure.
• Performed five procedures of artificial insemination.
• Assisted in designing embryo transfer protocols throughout one breeding season. • Assisted in embryo transfer procedures.
• Collected and prepared biological specimens for embryo transfer protocol.
", "Summer 2019", "Veterinary Assistant", "Tampico, Mexico",
  
) %>% 
  detailed_entries(Degree, Year, Institution, Where)
```

# Relevant Coursework

```{r}
library(tibble)
tribble(
  ~ Degree, ~ Year, ~ Institution, ~ Where,
 
    "• Collaborated in the creation of a working simulation designed to reinforce the understanding of students on Bacterial Selection and Bacterial Growth Curves.
• Bioinformatics skills: Python programming (functions, conditionals, dictionaries, exposure to BioPython). Tools to support laboratory work: Restriction Mapping (NEBCutter), Oligo Design (primer3, primerblast), Nucleotide Characterization (blast [n,p.x,tx, reciprocal blast for ortholog detection]).
", "2022", "Bioinformatics Project", "Seattle University",
  "• Performed a series of experiments to investigate the binding specificity of lectin concanavalin A in S. cerevisiae and E. coli with various sugars and presented findings in the form of a research article.
", "Summer 2021", "BIOL 4751 Cell Biology Independent Project", "Seattle University",
  
) %>% 
  detailed_entries(Degree, Year, Institution, Where)
```





# Engagements

```{r}
tribble(
  ~Year, ~Type, ~Desc,
  "2023", "Latine Student Organization", "",
  "2018-22", "Seattle University Women's Tennis Team", "",
  "2019-22", "Seattle University Dean and President List", ""
) %>% 
  brief_entries(
    glue::glue(" {Type}"),
    Year, 
    Desc
  )
```



