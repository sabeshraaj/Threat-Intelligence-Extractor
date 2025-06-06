# 🛡️ Threat Intelligence Extractor

A comprehensive cybersecurity tool that automatically extracts, analyzes, and visualizes threat intelligence from PDF reports using advanced AI and graph database technologies.

## 🌟 Features

### 📄 Automated PDF Processing
- **Smart Text Extraction**: Converts PDF threat reports to structured markdown
- **Image Preservation**: Extracts and saves embedded images at 300 DPI
- **Document Chunking**: Intelligently splits content for optimal processing

### 🔍 Multi-layered Intelligence Extraction
- **IoC Detection**: Automatically identifies IP addresses, domains, file hashes, and URLs
- **RAG-powered Analysis**: Uses AI to extract threat actors, TTPs, malware, and targets
- **MITRE ATT&CK Mapping**: Maps tactics and techniques to the MITRE framework

### 🧠 AI-Powered Analysis
- **Local LLM Integration**: Uses Ollama with Qwen2.5 model for privacy-focused analysis
- **Vector Similarity Search**: ChromaDB for intelligent document retrieval
- **Structured Output**: Generates clean JSON formatted intelligence data

### 🔗 Graph Database Integration
- **Neo4j Visualization**: Creates relationship graphs between threat entities
- **Cyber Kill Chain Mapping**: Visualizes attack patterns and relationships
- **Bulk Data Import**: Efficient storage of complex threat relationships

### 🦠 Malware Analysis
- **VirusTotal Integration**: Analyzes file hashes for malware detection
- **Multi-hash Support**: MD5, SHA1, SHA256, SHA512 hash analysis
- **Threat Scoring**: Provides malicious/suspicious verdict counts

### 🎨 Cyberpunk Interface
- **Responsive Design**: Modern web interface with cybersecurity aesthetics
- **Real-time Processing**: Live feedback during PDF analysis
- **Selective Export**: Choose specific intelligence types to export
- **Copy-to-Clipboard**: Easy data sharing and integration

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Web Interface │────│  Flask Backend   │────│   AI Pipeline   │
│   (Cyberpunk)   │    │  (main.py)       │    │  (RAG + LLM)    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                       ┌──────────────────┐    ┌─────────────────┐
                       │  PDF Processor   │    │  Vector Store   │
                       │  (pymupdf4llm)   │    │  (ChromaDB)     │
                       └──────────────────┘    └─────────────────┘
                                │                        │
                       ┌──────────────────┐    ┌─────────────────┐
                       │  IoC Extractor   │    │   Neo4j Graph   │
                       │  (ioc_finder)    │    │   Database      │
                       └──────────────────┘    └─────────────────┘
                                │
                       ┌──────────────────┐
                       │  VirusTotal API  │
                       │  (Hash Analysis) │
                       └──────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Ollama with Qwen2.5 model
- Neo4j Database (optional)
- VirusTotal API key

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/threat-intelligence-extractor.git
cd threat-intelligence-extractor
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
Create a `.env` file:
```env
virus_total_api_key=your_virustotal_api_key_here
```

4. **Start Ollama service**
```bash
ollama pull qwen2.5
ollama serve
```

5. **Configure Neo4j (Optional)**
Update credentials in `graph_neo4j.py`:
```python
neo4j = Neo4jConnector("bolt://localhost:7687", "neo4j", "password")
```

6. **Run the application**
```bash
python main.py
```

Visit `http://localhost:5000` to access the interface.

## 📊 Usage Examples

### 1. Processing a Threat Report

1. **Upload PDF**: Drag and drop your threat intelligence report
2. **Process Report**: Click "PROCESS REPORT" to begin analysis
3. **Select Intelligence Types**: Choose which data to extract and view
4. **Export Results**: Copy JSON data for integration with other tools

### 2. Viewing Extracted Intelligence

The system extracts and displays:
- **IoCs**: IP addresses, domains, file hashes, URLs
- **Threat Actors**: APT groups, cybercriminal organizations
- **TTPs**: MITRE ATT&CK tactics and techniques
- **Malware**: Malicious software families and variants
- **Targets**: Affected industries and organizations

### 3. Hash Analysis Results

VirusTotal integration provides:
- Malware detection verdicts
- File type identification
- Security vendor analysis
- Threat classification tags

### 4. Neo4j Graph Visualization

The graph database shows:
- **Threat Actor Relationships**: Connections between groups and activities
- **Attack Patterns**: How TTPs relate to specific threats
- **Infrastructure Links**: IoC relationships and overlaps
- **Target Analysis**: Which entities are most at risk

## 📈 Results
![Front End UI](Front%20End.jpg)

![Knowledge Base](Knowledge%20Base.jpg)

![Knowledge Graph](Knowledge%20Graph.jpg)


## 🛠️ Technology Stack

### Backend
- **Flask**: Web framework for API endpoints
- **LangChain**: Document processing and RAG pipeline
- **HuggingFace**: Text embeddings and transformers
- **ChromaDB**: Vector database for similarity search
- **Neo4j**: Graph database for relationship mapping

### AI/ML
- **Ollama**: Local LLM inference server
- **Qwen2.5**: Large language model for text analysis
- **all-mpnet-base-v2**: Sentence embedding model
- **ioc_finder**: Cybersecurity indicator extraction

### Frontend
- **HTML5/CSS3**: Modern web interface
- **JavaScript**: Interactive functionality
- **Tailwind CSS**: Utility-first styling framework
- **Cyberpunk Design**: Custom themed interface

### External APIs
- **VirusTotal**: Malware analysis and threat intelligence
- **pymupdf4llm**: PDF to markdown conversion

## 🔧 Configuration

### Environment Variables
```env
# VirusTotal API configuration
virus_total_api_key=your_api_key

# Ollama configuration (optional)
OLLAMA_BASE_URL=http://localhost:11434

# Neo4j configuration (optional)
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=password
```

### Ollama Model Setup
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull required model
ollama pull qwen2.5

# Start service
ollama serve
```

## 🎯 Use Cases

### 1. **Threat Analysts**
- Automated processing of daily threat reports
- Quick extraction of IoCs for blocklist updates
- Correlation analysis across multiple reports

### 2. **Security Operations Centers (SOC)**
- Rapid intelligence gathering from vendor reports
- Integration with SIEM systems via JSON export
- Threat hunting support with structured data

### 3. **Incident Response Teams**
- Fast attribution analysis from threat reports
- TTPs mapping for defensive strategy
- Malware family identification and tracking

### 4. **Threat Intelligence Platforms**
- Bulk processing of threat intelligence feeds
- Graph-based relationship analysis
- Automated intelligence enrichment

## 🔒 Security Considerations

- **Local Processing**: AI analysis runs locally for data privacy
- **No Data Retention**: Uploaded files are deleted after processing
- **API Key Protection**: Secure handling of VirusTotal credentials
- **Input Validation**: Comprehensive file type and size validation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- **MITRE ATT&CK Framework**: For cybersecurity taxonomy
- **Ollama Team**: For local LLM inference capabilities
- **LangChain Community**: For document processing tools
- **Neo4j**: For graph database technology
- **VirusTotal**: For malware analysis API

---

⚡ **Built for the cybersecurity community by threat hunters, for threat hunters.** ⚡
