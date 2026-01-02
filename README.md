# WSL Installation with Buffer Support

This repository contains a WSL (Windows Subsystem for Linux) installation script with built-in buffer support for optimized output handling.

## Features

- **Buffer Support**: Configurable output buffering for improved performance
- **Flexible Configuration**: Adjustable buffer size via command-line arguments
- **Buffer Management**: Enable/disable buffering and manual flush capabilities

## Usage

### Basic Installation
```bash
./wsl\ --installbidahs
```

### With Custom Buffer Size
```bash
./wsl\ --installbidahs -b 2048
```

### Command-Line Options

- `-b <size>`: Set buffer size in bytes (default: 4096)
- `-e`: Enable buffering explicitly
- `-f`: Disable buffering and flush immediately
- `-h`: Display help message

## Buffer Support Details

The script implements a buffering mechanism that:
1. Accumulates output messages in memory
2. Automatically flushes when buffer size threshold is reached
3. Can be manually flushed or disabled as needed
4. Improves performance by reducing I/O operations

### Buffer Functions

- `buffer_write()`: Write messages to buffer
- `buffer_flush()`: Flush buffer contents to output
- `buffer_enable()`: Enable buffering
- `buffer_disable()`: Disable buffering and flush

## Examples

### Default buffering (4096 bytes)
```bash
./wsl\ --installbidahs
```

### Custom buffer size (2048 bytes)
```bash
./wsl\ --installbidahs -b 2048
```

### Disable buffering
```bash
./wsl\ --installbidahs -f
```

## System Requirements

- Designed for Windows systems with WSL support
- Bash shell environment
- Appropriate permissions to execute the script

## Contributing

This is part of Jabidah's Creations Systems Hub Exchange.

## License

See repository license for details.
