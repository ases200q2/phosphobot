# Control AI robots with phospho

**phospho** (or **phosphobot**) is a software that lets you control robots, record data, train and use VLA (vision language action models).

<div align="center">

<a href="https://pypi.org/project/phosphobot/"><img src="https://img.shields.io/pypi/v/phosphobot?style=flat-square&label=pypi+phospho" alt="phosphobot Python package on PyPi"></a>
<a href="https://www.ycombinator.com/companies/phospho"><img src="https://img.shields.io/badge/Y%20Combinator-W24-orange?style=flat-square" alt="Y Combinator W24"></a>
<a href="https://discord.gg/cbkggY6NSK"><img src="https://img.shields.io/discord/1106594252043071509" alt="phospho discord"></a>

</div>

## Overview of phospho

- 🕹️ Control your robot with the keyboard, a leader arm, a Meta Quest headset or via API
- 📹 Teleoperate robots to record datasets in LeRobot dataset format
- 🤖 Train action models like ACT, gr00t n1 or Pi0
- 🔥 Use action models to control robots
- 💻 Runs on macOS, Linux and Windows
- 🦾 Compatible with the SO-100, SO-101, WX-250 and AgileX Piper
- 🔧 Extend it with your own robots and cameras

## Getting started with phosphobot

### 1. Get a SO-100 robot

Purchase your Phospho starter pack at [robots.phospho.ai](https://robots.phospho.ai) or build your own robot following the instructions in [the SO-100 repo](https://github.com/TheRobotStudio/SO-ARM100).

### 2. Install the phosphobot server

```bash
# Install it this way
curl -fsSL https://raw.githubusercontent.com/phospho-app/phosphobot/main/install.sh | bash
# Start it this way
phosphobot run
# Upgrade it with brew or with apt
# sudo apt update && sudo apt install phosphobot
# brew update && brew upgrade phosphobot
# powershell -ExecutionPolicy ByPass -Command "irm https://raw.githubusercontent.com/phospho-app/phosphobot/main/install.ps1 | iex"
```

This will:

- on mac: use brew to install phosphobot
- on linux: install phosphobot through apt
- on windows: install a .exe

### 3. Make your robot move for the first time!

Go to the webapp at `YOUR_SERVER_ADDRESS:YOUR_SERVER_PORT` (default is `localhost:80`) and click control.

You will be able to control your robot with:

- the keyboard
- a leader arm
- a Meta Quest if you have the phospho teleop app

> _Note: port 80 might already be in use, if that's the case, the server will spin up on localhost:8080_

### 4. Record a dataset

Record a 40 episodes dataset of the task you want the robot to learn.

Check out the [docs](https://docs.phospho.ai/basic-usage/dataset-recording) for more details.

### 5. Train an action model

To train an action model on the dataset you recorded, you can:

- train a model directly from the phosphobot webapp (see [this tutorial](https://docs.phospho.ai/basic-usage/training))
- use your own machine (see [this tutorial](tutorials/00_finetune_gr00t_vla.md) to finetune gr00t n1)

In both cases, you will have a trained model exported to huggingface.

To learn more about training action models for robotics, check out the [docs](https://docs.phospho.ai/basic-usage/training).

### 6. Use the model to control your robot

Now that you have a trained model hosted on huggingface, you can use it to control your robot either:

- directly from the webapp
- from your own code using the phosphobot python package (see [this script](scripts/quickstart_ai_gr00t.py) for an example)

Learn more [in the docs](https://docs.phospho.ai/basic-usage/inference).

Congrats! You just trained and used your first action model on a real robot.

## Examples

The `examples/` directory is the quickest way to see the toolkit in action. Check it out!
Proud of what you build? Share it with the community by opening a PR to add it to the `examples/` directory.

## Advanced Usage

You can directly call the phosphobot server from your own code, using the HTTP API and websocket API.

Go to the interactive docs of the API to use it interactively and learn more about it.
It is available at `YOUR_SERVER_ADDRESS:YOUR_SERVER_PORT/docs`. By default, it is available at `localhost:80/docs`.

We release new versions very often, so make sure to check the API docs for the latest features and changes.

## Supported Robots

We currently support the following robots:

- [SO-100](https://github.com/TheRobotStudio/SO-ARM100)
- [SO-101](https://github.com/TheRobotStudio/SO-ARM100)
- [Koch v1.1](https://github.com/jess-moss/koch-v1-1) (beta)
- WX-250 by Trossen Robotics (beta)
- [AgileX Piper](https://global.agilex.ai/products/piper) (Linux-only, beta)
- [Unitree Go2 Air, Pro, Edu](https://shop.unitree.com/en-fr/products/unitree-go2) (beta)
- [LeCabot](https://github.com/phospho-app/lecabot) (beta)

See this [README](phosphobot/README.md) for more details on how to add support for a new robots or open an issue.

## Join the Community

Connect with other developers and share your experience in our [Discord community](https://discord.gg/cbkggY6NSK)

## Install from source

0. (Recommended) Create a virtual environment and install the Python dependencies listed in `requirements.txt`:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

1. Download and install [uv](https://docs.astral.sh/uv/getting-started/installation/) and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm). Best compatibility is with `python>=3.10` and `node>=20`.

2. Clone github

```bash
git clone https://github.com/phospho-app/phosphobot.git
```

3. On MacOS and Windows, to build the frontend and start the backend, run:

```bash
make
```

On Windows, the Makefile don't work. You can run the commands directly.

```
cd ./dashboard && (npm i && npm run build && mkdir -p ../phosphobot/resources/dist/ && cp -r ./dist/* ../phosphobot/resources/dist/)
cd phosphobot && uv run --python 3.10 phosphobot run --simulation=headless
```

4. Go to `localhost:80` in your browser to see the dashboard or get the server infos with:

```bash
curl -X 'GET' 'http://localhost/status' -H 'accept: application/json'
```

If you only need a quick simulation test without building the dashboard you can now run:

```bash
uv pip install -e ./phosphobot   # or 'pip install -e ./phosphobot' if you skipped step 0
uv run phosphobot run --only-simulation --simulation=headless --port 8080 --no-telemetry
# Then open http://localhost:8080 in your browser.
```

> _Note: some features, such as connection to the phospho cloud, AI training, and AI control, are not available when installing from source._

## Troubleshooting

### ImportError: `av` (PyAV) missing

Encoding video files requires the optional [PyAV](https://github.com/PyAV-Org/PyAV) bindings and the FFmpeg development headers.  If you only want to **run the simulator or the HTTP server** you can ignore this warning—PyAV-dependent features are disabled automatically.

If you do need video support, first install the FFmpeg dev libs then PyAV:

```bash
# Debian / Ubuntu
sudo apt-get install -y libavformat-dev libavcodec-dev libavdevice-dev \
                       libavutil-dev libavfilter-dev libswscale-dev libswresample-dev

# Then (inside your venv)
pip install av --break-system-packages
```

### GUI mode on a headless server (no display)

The `--simulation=gui` option opens the PyBullet window which requires an X11 display.  On cloud VMs or CI runners you can emulate a display with `xvfb`:

```bash
sudo apt-get install -y xvfb
xvfb-run -s "-screen 0 1024x768x24" phosphobot run --only-simulation --simulation=gui
```

For automated testing you can stick to the default `--simulation=headless`.

### Missing low-level system libs / vendor SDKs (optional robots)
Certain robot back-ends (e.g. **Unitree GO2**, **Piper**, **SO-100**) ship
Python wrappers that depend on vendor SDKs or large native libraries.  When the
wrapper cannot be imported the simulator and core HTTP server will still work
— you will now just see a harmless warning:

```
ImportError: No module named 'go2_webrtc_driver'  # ignored
```

If you only care about the simulation you may safely ignore those messages.  A
real robot will, of course, require its corresponding SDK to be installed.

### `ModuleNotFoundError: netifaces / toml / serial / httpx`

These lightweight helper libraries are used to discover the local IP address
(`netifaces`), parse **pyproject.toml** files (`toml`), enumerate USB/Serial
ports (`pyserial`), or perform HTTP requests (`httpx`).

Install them with:

```bash
pip install --break-system-packages netifaces toml pyserial httpx
```

## Contributing

We welcome contributions! Some of the ways you can contribute:

- Add support for new AI models
- Add support for new teleoperation controllers
- Add support for new robots and sensors
- Add something you built to the examples
- Improve the dataset collection and manipulation
- Improve the [documentation and tutorials](https://github.com/phospho-app/docs)
- Improve code quality and refacto
- Improve the performance of the app
- Fix issues you faced

## Support

- **Documentation**: Read the [documentation](https://docs.phospho.ai)
- **Community Support**: Join our [Discord server](https://discord.gg/cbkggY6NSK)
- **Issues**: Submit problems or suggestions through [GitHub Issues](https://github.com/phospho-app/phosphobot/issues)

## License

MIT License

---

Made with 💚 by the Phospho community
