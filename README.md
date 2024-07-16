# A (Discord) Bot

This is a Discord bot.

## Description

Lorem ipsum etc etc [TODO]
  
## Getting Started

### Dependencies

<details>
<summary>Dependencies from requirements.txt</summary>

- `discord.py==2.4.0`
- `python-dotenv==1.0.1`
- `yt_dlp==2024.7.9`

</details>

<details>
<summary>Dependencies from environment.yml</summary>

- `aom=3.9.1=h7bae524_0`
- `bzip2=1.0.8=h99b78c6_7`
- `ca-certificates=2024.7.4=hf0a4a13_0`
- `cairo=1.18.0=hc6c324b_2`
- `dav1d=1.2.1=hb547adb_0`
- `expat=2.6.2=hebf3989_0`
- `ffmpeg=7.0.1=gpl_h5b99759_104`
- `font-ttf-dejavu-sans-mono=2.37=hab24e00_0`
- `font-ttf-inconsolata=3.000=h77eed37_0`
- `font-ttf-source-code-pro=2.038=h77eed37_0`
- `font-ttf-ubuntu=0.83=h77eed37_2`
- `fontconfig=2.14.2=h82840c6_0`
- `fonts-conda-ecosystem=1=0`
- `fonts-conda-forge=1=0`
- `freetype=2.12.1=hadb7bae_2`
- `fribidi=1.0.10=h27ca646_0`
- `gettext=0.22.5=h8fbad5d_2`
- `gettext-tools=0.22.5=h8fbad5d_2`
- `gmp=6.3.0=h7bae524_2`
- `gnutls=3.7.9=hd26332c_0`
- `graphite2=1.3.13=hebf3989_1003`
- `harfbuzz=9.0.0=h1836168_0`
- `icu=73.2=hc8870d7_0`
- `lame=3.100=h1a8c8d9_1003`
- `libabseil=20240116.2=cxx17_h00cdb27_1`
- `libasprintf=0.22.5=h8fbad5d_2`
- `libasprintf-devel=0.22.5=h8fbad5d_2`
- `libass=0.17.1=hf20b609_2`
- `libcxx=18.1.8=h167917d_0`
- `libexpat=2.6.2=hebf3989_0`
- `libffi=3.4.2=h3422bc3_5`
- `libgettextpo=0.22.5=h8fbad5d_2`
- `libgettextpo-devel=0.22.5=h8fbad5d_2`
- `libglib=2.80.3=h59d46d9_1`
- `libhwloc=2.11.1=default_h7685b71_1000`
- `libiconv=1.17=h0d3ecfb_2`
- `libidn2=2.3.7=h93a5062_0`
- `libintl=0.22.5=h8fbad5d_2`
- `libintl-devel=0.22.5=h8fbad5d_2`
- `libopenvino=2024.2.0=h5c9529b_1`
- `libopenvino-arm-cpu-plugin=2024.2.0=h5c9529b_1`
- `libopenvino-auto-batch-plugin=2024.2.0=hcd65546_1`
- `libopenvino-auto-plugin=2024.2.0=hcd65546_1`
- `libopenvino-hetero-plugin=2024.2.0=h88cb26a_1`
- `libopenvino-ir-frontend=2024.2.0=h88cb26a_1`
- `libopenvino-onnx-frontend=2024.2.0=h32b5460_1`
- `libopenvino-paddle-frontend=2024.2.0=h32b5460_1`
- `libopenvino-pytorch-frontend=2024.2.0=h00cdb27_1`
- `libopenvino-tensorflow-frontend=2024.2.0=h2741c3b_1`
- `libopenvino-tensorflow-lite-frontend=2024.2.0=h00cdb27_1`
- `libopus=1.3.1=h27ca646_1`
- `libpng=1.6.43=h091b4b1_0`
- `libprotobuf=4.25.3=hbfab5d5_0`
- `libsqlite=3.46.0=hfb93653_0`
- `libtasn1=4.19.0=h1a8c8d9_0`
- `libunistring=0.9.10=h3422bc3_0`
- `libvpx=1.14.1=h7bae524_0`
- `libxml2=2.12.7=h9a80f22_3`
- `libzlib=1.3.1=hfb2fe0b_1`
- `ncurses=6.5=hb89a1cb_0`
- `nettle=3.9.1=h40ed0f5_0`
- `openh264=2.4.1=hebf3989_0`
- `openssl=3.3.1=hfb2fe0b_1`
- `p11-kit=0.24.1=h29577a5_0`
- `pcre2=10.44=h297a79d_0`
- `pip=24.0=pyhd8ed1ab_0`
- `pixman=0.43.4=hebf3989_0`
- `pugixml=1.14=h13dd4ca_0`
- `python=3.12.4=h30c5eda_0_cpython`
- `readline=8.2=h92ec313_1`
- `setuptools=70.3.0=pyhd8ed1ab_0`
- `snappy=1.2.1=hd02b534_0`
- `svt-av1=2.1.2=h7bae524_0`
- `tbb=2021.12.0=h420ef59_3`
- `tk=8.6.13=h5083fa2_1`
- `tzdata=2024a=h0c530f3_0`
- `wheel=0.43.0=pyhd8ed1ab_1`
- `x264=1!164.3095=h57fd34a_2`
- `x265=3.5=hbc6ce65_3`
- `xz=5.2.6=h57fd34a_0`
- `zlib=1.3.1=hfb2fe0b_1`

</details>

### Installation

1. Go to the [Discord Developer Dashboard](https://discord.com/developers/applications) and create a new application
2. Customize **General information** and enable privleged intents in **Bot** menu. Get Bot Token via the *Reset Token* button.
3. In **OAuth2** menu, enable the scopes: ```bot applications.commands``` and give bot *Administrator* permissions. Follow *Guild Install* link to add bot to server.
5.  ```git clone https://github.com/alxdolphin/adiscordbot && cd adiscordbot && echo 'TOKEN="<TOKEN>"' > .env```

### Usage

Use Python environment manager of choice, like [Miniconda](https://docs.anaconda.com/miniconda/) or [Micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html)

```conda env create -f environment.yml && conda activate discordbot && pip install -r requirements.txt```

You can then run the bot with ```python bot.py```

## Version History

* **0.1**
    * Initial Commit

## Acknowledgments

* [README Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
