# Maniq - Manim Quality Stress Testing Tool

[![PyPI](https://img.shields.io/pypi/v/maniq)](https://pypi.org/project/maniq/)
[![Python Versions](https://img.shields.io/pypi/pyversions/maniq)](https://pypi.org/project/maniq/)
[![License](https://img.shields.io/pypi/l/maniq)](https://github.com/MarkHoo/maniq/blob/main/LICENSE)

Maniq is a comprehensive stress testing tool for Manim that helps you determine the maximum concurrent rendering capacity of your server across different quality levels with intelligent resource management to prevent system crashes.

## 🌟 Features

- **Multi-quality support**: Test 5 quality levels from 480p to 4K
  - Low quality (480p) - `l`/`low`
  - Medium quality (720p) - `m`/`medium`  
  - High quality (1080p) - `h`/`high`
  - 2K quality (1440p) - `p`/`2k`
  - 4K quality (2160p) - `k`/`4k`

- **Intelligent resource management**: 
  - Dynamically adjusts concurrency based on historical CPU usage
  - Prevents server crashes by monitoring system resources
  - Automatically pauses when CPU or memory usage exceeds 90%

- **Comprehensive analysis**:
  - Render time statistics (average, min, max, median, standard deviation)
  - Video duration and file size analysis
  - System resource usage monitoring (CPU, memory)

- **Multi-language support**: 
  - English (`en`)
  - Simplified Chinese (`zh`)
  - Traditional Chinese (`zh_tw`)
  - Korean (`ko`)
  - Japanese (`ja`)
  - German (`de`)
  - French (`fr`)
  - Spanish (`es`)
  - Russian (`ru`)

- **Professional reporting**:
  - Properly aligned tables that handle CJK characters correctly
  - Detailed text and JSON reports
  - Individual task logs with complete output

- **Flexible configuration**:
  - Customizable task launch intervals
  - Selectable quality levels
  - Configurable output directories

## 📦 Installation

### Prerequisites

- Python 3.10 or higher
- Manim installed and configured
- `ffprobe` (optional, for detailed video analysis)

### Install from PyPI

```bash
pip install -U maniq
```

### Install from source

```bash
git clone https://github.com/MarkHoo/maniq.git
cd maniq
pip install .
```

## 🚀 Quick Start

### Basic usage

```bash
# Test all quality levels with default settings
maniq /path/to/your/manim/code

# View version information
maniq -V
maniq --version
```

### Common examples

```bash
# Test only high quality and 4K with 2-second intervals
maniq /path/to/manim/code -q h k -i 2.0

# Test low and medium quality in Chinese
maniq /path/to/manim/code -q l m --lang zh

# Custom output directories and test duration
maniq /path/to/manim/code -o my_output -d 1200 --lang ja

# Mix short and full quality names
maniq /path/to/manim/code -q low m 2k k --lang ko
```

## 📋 Command Line Options

### Version and Help

| Option | Description |
|--------|-------------|
| `-V`, `--version` | Show version information and exit |
| `-h`, `--help` | Show help message and exit |

### Quality Selection

| Option | Short | Description | Values |
|--------|-------|-------------|--------|
| `--qualities` | `-q` | Quality levels to test | `l`/`low`, `m`/`medium`, `h`/`high`, `p`/`2k`, `k`/`4k` |

### Configuration

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--output-dir` | `-o` | Render output directory | `manim_quality_output` |
| `--log-output-dir` | `-l` | Task log output directory | `manim_task_logs` |
| `--max-duration` | `-d` | Max test duration per quality (seconds) | `1800` |
| `--launch-interval` | `-i` | Task launch interval (seconds) | `1.0` |
| `--report-file` | `-r` | Text report filename | `manim_quality_test_report.txt` |
| `--json-report` | `-j` | JSON report filename | `manim_quality_test_results.json` |
| `--log-file` | | Main log filename | `manim_quality_stress_test.log` |
| `--lang`, `--language` | | Report and log language | `en` |

## 🌍 Language Support

Maniq supports 9 languages with complete translation of all messages and reports:

| Language | Code | Quality Names |
|----------|------|---------------|
| English | `en` | LOW, MEDIUM, HIGH, 2K, 4K |
| Simplified Chinese | `zh` | 低质量, 中质量, 高质量, 2K, 4K |
| Traditional Chinese | `zh_tw` | 低品質, 中品質, 高品質, 2K, 4K |
| Korean | `ko` | 저품질, 중품질, 고품질, 2K, 4K |
| Japanese | `ja` | 低品質, 中品質, 高品質, 2K, 4K |
| German | `de` | NIEDRIG, MITTEL, HOCH, 2K, 4K |
| French | `fr` | BASSE, MOYENNE, HAUTE, 2K, 4K |
| Spanish | `es` | BAJA, MEDIA, ALTA, 2K, 4K |
| Russian | `ru` | НИЗКОЕ, СРЕДНЕЕ, ВЫСОКОЕ, 2K, 4K |

## 📊 Output Files

After running Maniq, you'll get the following output files:

### Reports
- **Text Report** (`manim_quality_test_report.txt`): Comprehensive human-readable report with properly aligned tables
- **JSON Report** (`manim_quality_test_results.json`): Structured data for programmatic analysis

### Logs
- **Main Log** (`manim_quality_stress_test.log`): Complete execution log with timestamps
- **Task Logs** (`manim_task_logs/`): Individual logs for each render task containing:
  - Full command output (stdout/stderr)
  - System resource usage before and after
  - Video file information (if available)
  - Execution timing details

### Render Output
- **Rendered Videos** (`manim_quality_output/`): Actual rendered video files organized by quality and task ID

## 📈 Sample Report

```
MANIQ - Manim Quality Stress Testing Report
======================================================================================================================

Performance Comparison Summary
+------------+--------------+--------------+------------------+--------------------+------------------+
| Quality    | Max Concurrent | Success Rate | Avg Render Time  | Avg Video Duration | Avg File Size (MB) |
+------------+--------------+--------------+------------------+--------------------+------------------+
| LOW        |            8 |       100.00%|             3.45 |               2.10 |             1.25 |
| MEDIUM     |            6 |       100.00%|             5.67 |               2.10 |             3.42 |
| HIGH       |            4 |       100.00%|             8.92 |               2.10 |             7.85 |
| 2K         |            2 |       100.00%|            15.34 |               2.10 |            18.67 |
| 4K         |            1 |       100.00%|            28.76 |               2.10 |            45.23 |
+------------+--------------+--------------+------------------+--------------------+------------------+
```

## 🛠️ Intelligent Resource Management

Maniq uses a sophisticated algorithm to prevent system overload:

1. **Initial Phase**: Starts tasks with the specified interval
2. **Monitoring**: Tracks CPU and memory usage of completed tasks
3. **Dynamic Adjustment**: Calculates average CPU usage per task
4. **Safety Check**: Before starting a new task, ensures:
   - Remaining CPU ≥ (Average CPU usage + 5%)
   - CPU usage < 90%
   - Memory usage < 90%
5. **Automatic Pause**: Waits for resources to become available if limits are exceeded

This ensures your server remains responsive and doesn't crash during intensive testing.

## 🔧 Requirements

### Python Dependencies
- `psutil>=7.0.0` - System resource monitoring

### System Dependencies
- **Manim** - The animation engine being tested
- **ffprobe** (optional) - For detailed video analysis (part of ffmpeg)

### Hardware Recommendations
- **Minimum**: 4 CPU cores, 8GB RAM
- **Recommended**: 8+ CPU cores, 16+ GB RAM for 4K testing
- **Storage**: Sufficient disk space for rendered videos (4K videos can be large)

## 🐛 Troubleshooting

### Common Issues

**"No .py files found" error**
- Ensure your code directory contains Manim `.py` files
- Verify the path is correct and accessible

**Tasks failing with timeout**
- Increase `--max-duration` for higher quality levels
- 4K rendering may take longer than the default 20-minute timeout

**Poor performance or crashes**
- Reduce `--launch-interval` to start tasks less frequently
- Test fewer quality levels simultaneously
- Ensure sufficient system resources are available

**CJK characters not displaying properly**
- Ensure your terminal supports UTF-8 encoding
- The tables are properly aligned regardless of character display

### Debugging

- Check the main log file for detailed error messages
- Review individual task logs in `manim_task_logs/` directory
- Monitor system resources during testing using `htop` or similar tools

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built on top of the amazing [Manim](https://www.manim.community/) animation engine
- Uses [psutil](https://github.com/giampaolo/psutil) for system monitoring
- Inspired by the need for reliable performance testing in production environments

## 📬 Feedback and Contributions

We welcome feedback, bug reports, and contributions! Please open an issue or pull request on our [GitHub repository](https://github.com/MarkHoo/maniq).

---

**Maniq** - Because knowing your server's limits shouldn't crash your server! 🚀
