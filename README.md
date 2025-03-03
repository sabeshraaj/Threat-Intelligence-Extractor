# Threat Intelligence Analysis

This repository contains scripts for extracting, analyzing, and visualizing threat intelligence data from various sources. The project involves fetching threat actor information, analyzing IoCs using VirusTotal, and storing threat intelligence data in a Neo4j database for visualization.

## Table of Contents
- [Files and Their Purpose](#files-and-their-purpose)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Files and Their Purpose

### 1. **hash_analysis.py**
   - Analyzes file hashes (MD5, SHA-1, SHA-256, SHA-512) using VirusTotal API.
   - Extracts threat intelligence data like malicious score, tags, TLSH, and file type.
   - Prints the extracted information in a structured format.

### 2. **graph_neo4j.py**
   - Connects to a Neo4j database and inserts threat intelligence data.
   - Constructs Cypher queries dynamically based on extracted parameters.
   - Stores threat actors, IoCs (IP addresses, domains), TTPs, malware, and targeted entities.

### 3. **ioc_extractor.py**
   - Extracts IoCs (Indicators of Compromise) such as IPs, hashes, and domains from input data.
   - Formats the extracted IoCs into a structured JSON format.

### 4. **threat_intel_parser.py**
   - Parses threat intelligence reports to extract meaningful threat indicators.
   - Processes structured and unstructured text to identify IoCs, TTPs, and threat actors.

### 5. **data_visualization.py**
   - Generates graphical representations of threat intelligence data using Neo4j.
   - Helps in visualizing relationships between threat actors, malware, and attack techniques.

### 6. **config.py**
   - Contains API keys and configuration settings for connecting to VirusTotal and Neo4j.
   - Stores database credentials securely.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/threat-intelligence.git
   cd threat-intelligence
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- **Hash Analysis:**
  ```bash
  python hash_analysis.py
  ```
- **Threat Intelligence Storage (Neo4j):**
  ```bash
  python graph_neo4j.py
  ```
- **IoC Extraction:**
  ```bash
  python ioc_extractor.py
  ```
- **Threat Report Parsing:**
  ```bash
  python threat_intel_parser.py
  ```
- **Data Visualization:**
  ```bash
  python data_visualization.py
  ```

## Dependencies

- Python 3.x
- `requests`
- `neo4j`
- `pandas`
- `matplotlib`

Install dependencies using:
```bash
pip install requests neo4j pandas matplotlib
```

## License
This project is licensed under the MIT License.

