[![send_newsletter](https://github.com/deep-diver/hf-daily-paper-newsletter/actions/workflows/newsletter.yml/badge.svg)](https://github.com/deep-diver/hf-daily-paper-newsletter/actions/workflows/newsletter.yml)

# Daily Newsletter for 🤗 Daily Papers 

[![Click to - Subscribe Newsletter](https://img.shields.io/badge/Click_to-Subscribe_Newsletter-2ea44f?style=for-the-badge)](https://groups.google.com/g/hf-daily-paper-newsletter)

This repository sends out a newsletter at `0 20 * * *` collected from [🤗 Daily Papers](https://huggingface.co/papers) to the subscribers. If you want to subscribe, please join the [newsletter group](https://groups.google.com/u/2/g/hf-daily-paper-newsletter
).

Everything is automated via GitHub Action, so no paid maintanance at all.

# How this works?

This whole project works in 2 steps broadly in the perspective of GitHub Action workflow.

1. [collect papers](https://github.com/deep-diver/hf-daily-paper-newsletter/blob/main/.github/workflows/collect_papers.yml)
    1. Download the metadat of daily papers from [🤗 Daily Papers](https://huggingface.co/papers) API Endpoint. The target date is the yesterday since it is unclear when the full list of daily paper is fully updated. The target date is dynamically calculated via `date` command.
    2. Run `go run main.go parse` command to **(1)** parse the downloaded the metadata file (JSON), **(2)** generate categories/tags of each paper via [Gemini API](https://ai.google.dev/), and **(3)** generate reformatted `yaml` file for each paper which is suitable for newsletter program. Each `yaml` file will be stored inside the `current` directory.
   
2. [send newsletter](https://github.com/deep-diver/hf-daily-paper-newsletter/blob/main/.github/workflows/newsletter.yml)
    1. Grasp all the `yaml` files from the `current` directory.
    2. Fill in the email HTML [template](https://github.com/deep-diver/hf-daily-paper-newsletter/tree/main/templates) with the contents from the `yaml` files.
    3. Archiving each papers' `yaml` file under the `archive` directory
    4. Generate markdown files based on the existing categories/tags. Add link of the corresponding archived paper `yaml` file to each markdown file.
    5. Send out email to the receivers which are specified in the [config.yaml](https://github.com/deep-diver/hf-daily-paper-newsletter/blob/main/configs.yaml) file.
    6. Clean up the `current` directory.

# Todos
- [ ] Auto Translation to other languages (first target -> Korean)
