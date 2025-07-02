# Phosphobot Repository Structure and Workflow Analysis

## Overview

**Phosphobot** (also known as **phosphobot**) is a comprehensive software platform for controlling robots, recording datasets, training Vision-Language-Action (VLA) models, and deploying AI-powered robotic control systems. The project is designed to bridge the gap between teleoperation, data collection, and AI model deployment for robotics applications.

## Top-Level Directory Structure

### Core Directories and Files

#### `/phosphobot/` - Main Source Code Directory
The primary Python package containing the core implementation:
- **Purpose**: Contains the main application logic, hardware interfaces, AI models, and API endpoints
- **Structure**: Organized into modular components for hardware control, camera management, AI inference, and web APIs
- **Key Components**:
  - `main.py` - Primary entry point with CLI interface
  - `app.py` - FastAPI application setup and configuration
  - `configs.py` - Configuration management system using YAML
  - Hardware abstraction layers for various robot types
  - AI model implementations and inference engines

#### `/dashboard/` - Frontend Web Interface
A modern React/TypeScript-based web dashboard:
- **Purpose**: Provides a user-friendly web interface for robot control, dataset recording, and model training
- **Technology Stack**: React, TypeScript, Vite, Tailwind CSS
- **Build System**: Uses npm/Node.js with Vite bundler
- **Integration**: Built assets are copied to `phosphobot/resources/dist/` for serving

#### `/scripts/` - Automation and Utility Scripts
Helper scripts for various tasks:
- **Purpose**: Contains automation scripts for data processing, model training, and robot-specific utilities
- **Contents**:
  - `quickstart_ai_gr00t.py` - Example script for AI-powered robot control using Gr00t models
  - `quickstart_ai_pi0.py` - Example for Pi0 model integration
  - `datasets/` - Dataset manipulation utilities
  - `feetech/` - Servo motor specific scripts

#### `/examples/` - Demonstration Projects
Real-world usage examples and tutorials:
- **Purpose**: Showcases different use cases and provides learning materials
- **Contents**:
  - Movement patterns (circles, squares)
  - Keyboard and voice control examples
  - Hand tracking and gesture recognition
  - Interactive games (rock-paper-scissors)

#### `/tutorials/` - Educational Content
Step-by-step guides and documentation:
- **Contents**: 
  - `00_finetune_gr00t_vla.md` - Comprehensive guide for fine-tuning Gr00t VLA models

#### `/inference/` - Model Inference Infrastructure
Dedicated inference servers and clients:
- **Purpose**: Provides inference capabilities for trained models
- **Models Supported**:
  - **ACT (Action Chunking with Transformers)**: Transformer-based action prediction
  - **Gr00t**: NVIDIA's humanoid robot foundation model
  - **Pi0**: Physical Intelligence's action models
- **Architecture**: Client-server model with dedicated GPU servers

#### `/docs/` - Documentation (External)
References external documentation repository for comprehensive guides.

### Configuration and Build Files

#### `pyproject.toml` - Python Project Configuration
- **Dependencies**: Extensive list including FastAPI, OpenCV, PyBullet, Hugging Face libraries
- **Robot Hardware Support**: Dynamixel SDK, Feetech servos, RealSense cameras
- **AI/ML Libraries**: PyTorch ecosystem, Hugging Face transformers and datasets
- **Development Tools**: pytest, mypy, ruff for code quality

#### `Makefile` - Build and Development Automation
- **Build Targets**:
  - `prod`: Production build with frontend compilation
  - `local`: Development server with debugging
  - `build_pyinstaller`: Creates standalone executable
- **Frontend Integration**: Automatically builds React dashboard and copies assets
- **Testing**: Provides test server configurations

#### `install.sh` / `install.ps1` - Installation Scripts
Platform-specific installation scripts for macOS, Linux, and Windows using package managers (brew, apt, PowerShell).

### Hardware and Model Support

#### Supported Robot Platforms
- **SO-100/SO-101**: Primary supported robotic arms
- **Koch v1.1**: Community-developed arm (beta)
- **WX-250**: Trossen Robotics arm (beta)
- **AgileX Piper**: Mobile manipulation platform (Linux-only)
- **Unitree Go2**: Quadruped robots (beta)
- **LeCabot**: Custom robot platform (beta)

#### AI Model Architectures
- **ACT (Action Chunking with Transformers)**: Sequence-to-sequence transformer for action prediction
- **Gr00t N1**: NVIDIA's foundation model for humanoid robots
- **Pi0**: Physical Intelligence's vision-language-action models

## Core Logic and Execution Workflow

### Main Entry Point: `phosphobot/main.py`

The application starts through a Typer-based CLI interface with the following initialization sequence:

1. **Environment Setup**:
   - Encoding fixes for Windows compatibility
   - Splash screen display with version information
   - Background version checking

2. **CLI Commands**:
   - `phosphobot run` - Starts the main server
   - `phosphobot info` - Hardware diagnostics
   - `phosphobot update` - Update instructions

### Server Initialization: `phosphobot/app.py`

The FastAPI application follows this startup sequence:

1. **Lifespan Management**:
   ```python
   @asynccontextmanager
   async def lifespan(app: FastAPI):
       # Initialize telemetry and crash reporting
       init_telemetry()
       # Initialize PyBullet simulation environment
       simulation_init()
       # Initialize camera systems
       cameras = get_all_cameras()
       # Initialize robot connection manager
       rcm = get_rcm()
       # Start UDP server for teleoperation
       udp_server = get_udp_server()
   ```

2. **Configuration Loading**:
   - YAML-based configuration system (`configs.py`)
   - Dynamic parameter adjustment
   - Hardware capability detection

3. **Module Initialization**:
   - **Camera System**: Multi-camera support with RealSense integration
   - **Robot Manager**: Hardware abstraction for different robot types
   - **AI Control**: Model loading and inference pipeline setup
   - **Recording System**: Dataset collection in LeRobot format

### Core Execution Flow

#### 1. Robot Control Pipeline

```python
# Hardware abstraction through base classes
BaseManipulator -> Specific robot implementations (SO100, Koch11, etc.)
```

**Control Modes**:
- **Manual Control**: Keyboard, leader-follower, VR headset
- **AI Control**: Model-driven autonomous operation
- **Gravity Compensation**: Physics-based assistance

#### 2. Data Recording Workflow

```python
# Recording pipeline
Recorder -> Dataset -> LeRobot format -> Hugging Face upload
```

**Process**:
1. Multi-camera synchronization
2. Joint state logging
3. Action sequence recording
4. Automatic dataset formatting
5. Cloud storage integration

#### 3. AI Model Training and Inference

**Training Pipeline**:
1. Dataset preparation in LeRobot format
2. Model configuration via experiment configs
3. Training on cloud infrastructure (Modal.com integration)
4. Model deployment to Hugging Face

**Inference Pipeline**:
1. Model server spawning (GPU-accelerated)
2. Real-time observation collection:
   ```python
   obs = {
       "video.image_cam_0": camera_frames,
       "state.arm": joint_positions,
       "annotation.human.action.task_description": task_text
   }
   ```
3. Action prediction and execution
4. Closed-loop control at 30Hz

### API Architecture

The system exposes RESTful APIs through FastAPI with the following endpoint categories:

- **`/control`**: Robot movement and positioning
- **`/camera`**: Image streaming and capture
- **`/recording`**: Dataset collection management
- **`/training`**: Model training orchestration
- **`/auth`**: Authentication and user management

### Configuration System

**YAML-based Configuration** (`configs.py`):
```yaml
# Example configuration
default_freq: 30
default_video_codec: "avc1"
default_video_size: [320, 240]
enable_realsense: true
simulation_mode: "headless"
```

**Dynamic Reconfiguration**: Settings can be modified at runtime through the web interface.

### Reproducibility and Development

#### Reproducibility Features
- **Deterministic Seeding**: Configurable random seeds for experiments
- **Checkpointing**: Automatic model and data checkpoints
- **Version Tracking**: Git integration and dependency pinning
- **Environment Isolation**: UV package manager for Python dependencies

#### Development Workflow
1. **Local Development**: `make local` for development server
2. **Testing**: Simulation mode with headless operation
3. **Production**: `make prod` for full deployment
4. **Profiling**: Built-in performance profiling with PyInstrument

### Framework Dependencies

**Core Frameworks**:
- **FastAPI**: Web API framework with automatic documentation
- **PyBullet**: Physics simulation for robot modeling
- **OpenCV**: Computer vision and image processing
- **Hugging Face**: Model hosting and dataset management
- **LeRobot**: Robotics-specific data formats and utilities

**Hardware Interfaces**:
- **Dynamixel SDK**: Servo motor control
- **RealSense SDK**: Depth camera integration
- **Feetech SDK**: Alternative servo control

### Extension and Customization

#### Adding New Robots
1. Implement `BaseManipulator` interface
2. Add hardware-specific communication protocols
3. Register in robot factory system
4. Update configuration schemas

#### Adding New AI Models
1. Implement `ActionModel` base class
2. Define model-specific configuration
3. Add inference server integration
4. Update spawn configuration system

#### Custom Teleoperation
1. Implement control signal interfaces
2. Add input device handlers
3. Integrate with existing control pipeline

## Summary

Phosphobot represents a comprehensive robotics development platform that seamlessly integrates:

1. **Hardware Abstraction**: Support for multiple robot platforms through unified interfaces
2. **Data Pipeline**: Complete workflow from teleoperation to dataset creation
3. **AI Integration**: State-of-the-art VLA models with easy deployment
4. **User Experience**: Modern web interface for non-technical users
5. **Developer Tools**: Extensive APIs and configuration options for customization

The modular architecture allows developers to extend the system with new robots, AI models, or control modalities while maintaining compatibility with the existing ecosystem. The emphasis on reproducibility and standardized data formats (LeRobot) makes it valuable for both research and production robotics applications.