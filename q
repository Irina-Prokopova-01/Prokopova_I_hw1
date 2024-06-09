[1mdiff --git a/.flake8 b/.flake8[m
[1mnew file mode 100644[m
[1mindex 0000000..791f075[m
[1m--- /dev/null[m
[1m+++ b/.flake8[m
[36m@@ -0,0 +1,2 @@[m
[32m+[m[32m[flake8][m
[32m+[m[32mmax-line-length = 119[m
[1mdiff --git a/.gitignore b/.gitignore[m
[1mnew file mode 100644[m
[1mindex 0000000..1f5819b[m
[1m--- /dev/null[m
[1m+++ b/.gitignore[m
[36m@@ -0,0 +1,163 @@[m
[32m+[m[32m# Byte-compiled / optimized / DLL files[m
[32m+[m[32m__pycache__/[m
[32m+[m[32m*.py[cod][m
[32m+[m[32m*$py.class[m
[32m+[m
[32m+[m[32m# C extensions[m
[32m+[m[32m*.so[m
[32m+[m
[32m+[m[32m# Distribution / packaging[m
[32m+[m[32m.Python[m
[32m+[m[32mbuild/[m
[32m+[m[32mdevelop-eggs/[m
[32m+[m[32mdist/[m
[32m+[m[32mdownloads/[m
[32m+[m[32meggs/[m
[32m+[m[32m.eggs/[m
[32m+[m[32mlib/[m
[32m+[m[32mlib64/[m
[32m+[m[32mparts/[m
[32m+[m[32msdist/[m
[32m+[m[32mvar/[m
[32m+[m[32mwheels/[m
[32m+[m[32mshare/python-wheels/[m
[32m+[m[32m*.egg-info/[m
[32m+[m[32m.installed.cfg[m
[32m+[m[32m*.egg[m
[32m+[m[32mMANIFEST[m
[32m+[m
[32m+[m[32m# PyInstaller[m
[32m+[m[32m#  Usually these files are written by a python script from a template[m
[32m+[m[32m#  before PyInstaller builds the exe, so as to inject date/other infos into it.[m
[32m+[m[32m*.manifest[m
[32m+[m[32m*.spec[m
[32m+[m
[32m+[m[32m# Installer logs[m
[32m+[m[32mpip-log.txt[m
[32m+[m[32mpip-delete-this-directory.txt[m
[32m+[m
[32m+[m[32m# Unit test / coverage reports[m
[32m+[m[32mhtmlcov/[m
[32m+[m[32m.tox/[m
[32m+[m[32m.nox/[m
[32m+[m[32m.coverage[m
[32m+[m[32m.coverage.*[m
[32m+[m[32m.cache[m
[32m+[m[32mnosetests.xml[m
[32m+[m[32mcoverage.xml[m
[32m+[m[32m*.cover[m
[32m+[m[32m*.py,cover[m
[32m+[m[32m.hypothesis/[m
[32m+[m[32m.pytest_cache/[m
[32m+[m[32mcover/[m
[32m+[m
[32m+[m[32m# Translations[m
[32m+[m[32m*.mo[m
[32m+[m[32m*.pot[m
[32m+[m
[32m+[m[32m# Django stuff:[m
[32m+[m[32m*.log[m
[32m+[m[32mlocal_settings.py[m
[32m+[m[32mdb.sqlite3[m
[32m+[m[32mdb.sqlite3-journal[m
[32m+[m
[32m+[m[32m# Flask stuff:[m
[32m+[m[32minstance/[m
[32m+[m[32m.webassets-cache[m
[32m+[m
[32m+[m[32m# Scrapy stuff:[m
[32m+[m[32m.scrapy[m
[32m+[m
[32m+[m[32m# Sphinx documentation[m
[32m+[m[32mdocs/_build/[m
[32m+[m
[32m+[m[32m# PyBuilder[m
[32m+[m[32m.pybuilder/[m
[32m+[m[32mtarget/[m
[32m+[m
[32m+[m[32m# Jupyter Notebook[m
[32m+[m[32m.ipynb_checkpoints[m
[32m+[m
[32m+[m[32m# IPython[m
[32m+[m[32mprofile_default/[m
[32m+[m[32mipython_config.py[m
[32m+[m
[32m+[m[32m# pyenv[m
[32m+[m[32m#   For a library or package, you might want to ignore these files since the code is[m
[32m+[m[32m#   intended to run in multiple environments; otherwise, check them in:[m
[32m+[m[32m# .python-version[m
[32m+[m
[32m+[m[32m# pipenv[m
[32m+[m[32m#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.[m
[32m+[m[32m#   However, in case of collaboration, if having platform-specific dependencies or dependencies[m
[32m+[m[32m#   having no cross-platform support, pipenv may install dependencies that don't work, or not[m
[32m+[m[32m#   install all needed dependencies.[m
[32m+[m[32m#Pipfile.lock[m
[32m+[m
[32m+[m[32m# poetry[m
[32m+[m[32m#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.[m
[32m+[m[32m#   This is especially recommended for binary packages to ensure reproducibility, and is more[m
[32m+[m[32m#   commonly ignored for libraries.[m
[32m+[m[32m#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control[m
[32m+[m[32m#poetry.lock[m
[32m+[m
[32m+[m[32m# pdm[m
[32m+[m[32m#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.[m
[32m+[m[32m#pdm.lock[m
[32m+[m[32m#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it[m
[32m+[m[32m#   in version control.[m
[32m+[m[32m#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control[m
[32m+[m[32m.pdm.toml[m
[32m+[m[32m.pdm-python[m
[32m+[m[32m.pdm-build/[m
[32m+[m
[32m+[m[32m# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm[m
[32m+[m[32m__pypackages__/[m
[32m+[m
[32m+[m[32m# Celery stuff[m
[32m+[m[32mcelerybeat-schedule[m
[32m+[m[32mcelerybeat.pid[m
[32m+[m
[32m+[m[32m# SageMath parsed files[m
[32m+[m[32m*.sage.py[m
[32m+[m
[32m+[m[32m# Environments[m
[32m+[m[32m.env[m
[32m+[m[32m.venv[m
[32m+[m[32menv/[m
[32m+[m[32mvenv/[m
[32m+[m[32mENV/[m
[32m+[m[32menv.bak/[m
[32m+[m[32mvenv.bak/[m
[32m+[m
[32m+[m[32m# Spyder project settings[m
[32m+[m[32m.spyderproject[m
[32m+[m[32m.spyproject[m
[32m+[m
[32m+[m[32m# Rope project settings[m
[32m+[m[32m.ropeproject[m
[32m+[m
[32m+[m[32m# mkdocs documentation[m
[32m+[m[32m/site[m
[32m+[m
[32m+[m[32m# mypy[m
[32m+[m[32m.mypy_cache/[m
[32m+[m[32m.dmypy.json[m
[32m+[m[32mdmypy.json[m
[32m+[m
[32m+[m[32m# Pyre type checker[m
[32m+[m[32m.pyre/[m
[32m+[m
[32m+[m[32m# pytype static type analyzer[m
[32m+[m[32m.pytype/[m
[32m+[m
[32m+[m[32m# Cython debug symbols[m
[32m+[m[32mcython_debug/[m
[32m+[m
[32m+[m[32m# PyCharm[m
[32m+[m[32m#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can[m
[32m+[m[32m#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore[m
[32m+[m[32m#  and can be added to the global gitignore or merged into this file.  For a more nuclear[m
[32m+[m[32m#  option (not recommended) you can uncomment the following to ignore the entire idea folder.[m
[32m+[m[32m.idea/[m
[32m+[m[32m.idea/[m
[1mdiff --git a/poetry.lock b/poetry.lock[m
[1mnew file mode 100644[m
[1mindex 0000000..a9f2050[m
[1m--- /dev/null[m
[1m+++ b/poetry.lock[m
[36m@@ -0,0 +1,244 @@[m
[32m+[m[32m# This file is automatically @generated by Poetry 1.8.3 and should not be changed by hand.[m
[32m+[m
[32m+[m[32m[[package]][m
[32m+[m[32mname = "black"[m
[32m+[m[32mversion = "24.4.2"[m
[32m+[m[32mdescription = "The uncompromising code formatter."[m
[32m+[m[32moptional = false[m
[32m+[m[32mpython-versions = ">=3.8"[m
[32m+[m[32mfiles = [[m
[32m+[m[32m    {file = "black-24.4.2-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:dd1b5a14e417189db4c7b64a6540f31730713d173f0b63e55fabd52d61d8fdce"},[m
[32m+[m[32m    {file = "black-24.4.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:8e537d281831ad0e71007dcdcbe50a71470b978c453fa41ce77186bbe0ed6021"},[m
[32m+[m[32m    {file = "black-24.4.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:eaea3008c281f1038edb473c1aa8ed8143a5535ff18f978a318f10302b254063"},[m
[32m+[m[32m    {file = "black-24.4.2-cp310-cp310-win_amd64.whl", hash = "sha256:7768a0dbf16a39aa5e9a3ded568bb545c8c2727396d063bbaf847df05b08cd96"},[m
[32m+[m[32m    {file = "black-24.4.2-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:257d724c2c9b1660f353b36c802ccece186a30accc7742c176d29c146df6e474"},[m
[32m+[m[32m    {file = "black-24.4.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:bdde6f877a18f24844e381d45e9947a49e97933573ac9d4345399be37621e26c"},[m
[32m+[m[32m    {file = "black-24.4.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e151054aa00bad1f4e1f04919542885f89f5f7d086b8a59e5000e6c616896ffb"},[m
[32m+[m[32m    {file = "black-24.4.2-cp311-cp311-win_amd64.whl", hash = "sha256:7e122b1c4fb252fd85df3ca93578732b4749d9be076593076ef4d07a0233c3e1"},[m
[32m+[m[32m    {file = "black-24.4.2-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:accf49e151c8ed2c0cdc528691838afd217c50412534e876a19270fea1e28e2d"},[m
[32m+[m[32m    {file = "black-24.4.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:88c57dc656038f1ab9f92b3eb5335ee9b021412feaa46330d5eba4e51fe49b04"},[m
[32m+[m[32m    {file = "black-24.4.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:be8bef99eb46d5021bf053114442914baeb3649a89dc5f3a555c88737e5e98fc"},[m
[32m+[m[32m    {file = "black-24.4.2-cp312-cp312-win_amd64.whl", hash = "sha256:415e686e87dbbe6f4cd5ef0fbf764af7b89f9057b97c908742b6008cc554b9c0"},[m
[32m+[m[32m    {file = "black-24.4.2-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:bf10f7310db693bb62692609b397e8d67257c55f949abde4c67f9cc574492cc7"},[m
[32m+[m[32m    {file = "black-24.4.2-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:98e123f1d5cfd42f886624d84464f7756f60ff6eab89ae845210631714f6db94"},[m
[32m+[m[32m    {file = "black-24.4.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:48a85f2cb5e6799a9ef05347b476cce6c182d6c71ee36925a6c194d074336ef8"},[m
[32m+[m[32m    {file = "black-24.4.2-cp38-cp38-win_amd64.whl", hash = "sha256:b1530ae42e9d6d5b670a34db49a94115a64596bc77710b1d05e9801e62ca0a7c"},[m
[32m+[m[32m    {file = "black-24.4.2-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:37aae07b029fa0174d39daf02748b379399b909652a806e5708199bd93899da1"},[m
[32m+[m[32m    {file = "black-24.4.2-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:da33a1a5e49c4122ccdfd56cd021ff1ebc4a1ec4e2d01594fef9b6f267a9e741"},[m
[32m+[m[32m    {file = "black-24.4.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ef703f83fc32e131e9bcc0a5094cfe85599e7109f896fe8bc96cc402f3eb4b6e"},[m
[32m+[m[32m    {file = "black-24.4.2-cp39-cp39-win_amd64.whl", hash = "sha256:b9176b9832e84308818a99a561e90aa479e73c523b3f77afd07913380ae2eab7"},[m
[32m+[m[32m    {file = "black-24.4.2-py3-none-any.whl", hash = "sha256:d36ed1124bb81b32f8614555b34cc4259c3fbc7eec17870e8ff8ded335b58d8c"},[m
[32m+[m[32m    {file = "black-24.4.2.tar.gz", hash = "sha256:c872b53057f000085da66a19c55d68f6f8ddcac2642392ad3a355878406fbd4d"},[m
[32m+[m[32m][m
[32m+[m
[32m+[m[32m[package.dependencies][m
[32m+[m[32mclick = ">=8.0.0"[m
[32m+[m[32mmypy-extensions = ">=0.4.3"[m
[32m+[m[32mpackaging = ">=22.0"[m
[32m+[m[32mpathspec = ">=0.9.0"[m
[32m+[m[32mplatformdirs = ">=2"[m
[32m+[m
[32m+[m[32m[package.extras][m
[32m+[m[32mcolorama = ["colorama (>=0.4.3)"][m
[32m+[m[32md = ["aiohttp (>=3.7.4)", "aiohttp (>=3.7.4,!=3.9.0)"][m
[32m+[m[32mjupyter = ["ipython (>=7.8.0)", "tokenize-rt (>=3.2.0)"][m
[32m+[m[32muvloop = ["uvloop (>=0.15.2)"][m
[32m+[m
[32m+[m[32m[[package]][m
[32m+[m[32mname = "click"[m
[32m+[m[32mversion = "8.1.7"[m
[32m+[m[32mdescription = "Composable command line interface toolkit"[m
[32m+[m[32moptional = false[m
[32m+[m[32mpython-versions = ">=3.7"[m
[32m+[m[32mfiles = [[m
[32m+[m[32m    {file = "click-8.1.7-py3-none-any.whl", hash = "sha256:ae74fb96c20a0277a1d615f1e4d73c8414f5a98db8b799a7931d1582f3390c28"},[m
[32m+[m[32m    {file = "click-8.1.7.tar.gz", hash = "sha256:ca9853ad459e787e2192211578cc907e7594e294c7ccc834310722b41b9ca6de"},[m
[32m+[m[32m][m
[32m+[m
[32m+[m[32m[package.dependencies][m
[32m+[m[32mcolorama = {version = "*", markers = "platform_system == \"Windows\""}[m
[32m+[m
[32m+[m[32m[[package]][m
[32m+[m[32mname = "colorama"[m
[32m+[m[32mversion = "0.4.6"[m
[32m+[m[32mdescription = "Cross-platform colored terminal text."[m
[32m+[m[32moptional = false[m
[32m+[m[32mpython-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"[m
[32m+[m[32mfiles = [[m
[32m+[m[32m    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},[m
[32m+[m[32m    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},[m
[32m+[m[32m][m
[32m+[m
[32m+[m[32m[[package]][m
[32m+[m[32mname = "flake8"[m
[32m+[m[32mversion = "7.0.0"[m
[32m+[m[32mdescription = "the modular source code checker: pep8 pyflakes and co"[m
[32m+[m[32moptional = false[m
[32m+[m[32mpython-versions = ">=3.8.1"[m
[32m+[m[32mfiles = [[m
[32m+[m[32m    {file = "flake8-7.0.0-py2.py3-none-any.whl", hash = "sha256:a6dfbb75e03252917f2473ea9653f7cd799c3064e54d4c8140044c5c065f53c3"},[m
[32m+[m[32m    {file = "flake8-7.0.0.tar.gz", hash = "sha256:33f96621059e65eec474169085dc92bf26e7b2d47366b70be2f67ab80dc25132"},[m
[32m+[m[32m][m
[32m+[m
[32m+[m[32m[package.dependencies][m
[32m+[m[32mmccabe = ">=0.7.0,<0.8.0"[m
[32m+[m[32mpycodestyle = ">=2.11.0,<2.12.0"[m
[32m+[m[32mpyflakes = ">=3.2.0,<3.3.0"[m
[32m+[m
[32m+[m[32m[[package]][m
[32m+[m[32mname = "isort"[m
[32m+[m[32mversion = "5.13.2"[m
[32m+[m[32mdescription = "A Python utility / library to sort Python imports."[m
[32m+[m[32moptional = false[m
[32m+[m[32mpython-versions = ">=3.8.0"[m
[32m+[m[32mfiles = [[m
[32m+[m[32m    {file = "isort-5.13.2-py3-none-any.whl", hash = "sha256:8ca5e72a8d85860d5a3fa69b8745237f2939afe12dbf656afbcb47fe72d947a6"},[m
[32m+[m[32m    {file = "isort-5.13.2.tar.gz", hash = "sha256:48fdfcb9face5d58a4f6dde2e72a1fb8dcaf8ab26f95ab49fab84c2ddefb0109"},[m
[32m+[m[32m][m
[32m+[m
[32m+[m[32m[package.extras][m
[32m+[m[32mcolors = ["colorama (>=0.4.6)"][m
[32m+[m
[32m+[m[32m[[package]][m
[32m+[m[32mname = "mccabe"[m
[32m+[m[32mversion = "0.7.0"[m
[32m+[m[32mdescription = "McCabe checker, plugin for flake8"[m
[32m+[m[32moptional = false[m
[32m+[m[32mpython-versions = ">=3.6"[m
[32m+[m[32mfiles = [[m
[32m+[m[32m    {file = "mccabe-0.7.0-py2.py3-none-any.whl", hash = "sha256:6c2d30ab6be0e4a46919781807b4f0d834ebdd6c6e3dca0bda5a15f863427b6e"},[m
[32m+[m[32m    {file = "mccabe-0.7.0.tar.gz", hash = "sha256:348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325"},[m
[32m+[m[32m][m
[32m+[m
[32m+[m[32m[[package]][m
[32m+[m[32mname = "mypy"[m
[32m+[m[32mversion = "1.10.0"[m
[32m+[m[32mdescription = "Optional static typing for Python"[m
[32m+[m[32moptional = false[m
[32m+[m[32mpython-versions = ">=3.8"[m
[32m+[m[32mfiles = [[m
[32m+[m[32m    {file = "mypy-1.10.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:da1cbf08fb3b851ab3b9523a884c232774008267b1f83371ace57f412fe308c2"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:12b6bfc1b1a66095ab413160a6e520e1dc076a28f3e22f7fb25ba3b000b4ef99"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9e36fb078cce9904c7989b9693e41cb9711e0600139ce3970c6ef814b6ebc2b2"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:2b0695d605ddcd3eb2f736cd8b4e388288c21e7de85001e9f85df9187f2b50f9"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp310-cp310-win_amd64.whl", hash = "sha256:cd777b780312ddb135bceb9bc8722a73ec95e042f911cc279e2ec3c667076051"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:3be66771aa5c97602f382230165b856c231d1277c511c9a8dd058be4784472e1"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:8b2cbaca148d0754a54d44121b5825ae71868c7592a53b7292eeb0f3fdae95ee"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1ec404a7cbe9fc0e92cb0e67f55ce0c025014e26d33e54d9e506a0f2d07fe5de"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:e22e1527dc3d4aa94311d246b59e47f6455b8729f4968765ac1eacf9a4760bc7"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp311-cp311-win_amd64.whl", hash = "sha256:a87dbfa85971e8d59c9cc1fcf534efe664d8949e4c0b6b44e8ca548e746a8d53"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:a781f6ad4bab20eef8b65174a57e5203f4be627b46291f4589879bf4e257b97b"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:b808e12113505b97d9023b0b5e0c0705a90571c6feefc6f215c1df9381256e30"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8f55583b12156c399dce2df7d16f8a5095291354f1e839c252ec6c0611e86e2e"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:4cf18f9d0efa1b16478c4c129eabec36148032575391095f73cae2e722fcf9d5"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp312-cp312-win_amd64.whl", hash = "sha256:bc6ac273b23c6b82da3bb25f4136c4fd42665f17f2cd850771cb600bdd2ebeda"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:9fd50226364cd2737351c79807775136b0abe084433b55b2e29181a4c3c878c0"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:f90cff89eea89273727d8783fef5d4a934be2fdca11b47def50cf5d311aff727"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fcfc70599efde5c67862a07a1aaf50e55bce629ace26bb19dc17cece5dd31ca4"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:075cbf81f3e134eadaf247de187bd604748171d6b79736fa9b6c9685b4083061"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp38-cp38-win_amd64.whl", hash = "sha256:3f298531bca95ff615b6e9f2fc0333aae27fa48052903a0ac90215021cdcfa4f"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:fa7ef5244615a2523b56c034becde4e9e3f9b034854c93639adb667ec9ec2976"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:3236a4c8f535a0631f85f5fcdffba71c7feeef76a6002fcba7c1a8e57c8be1ec"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:4a2b5cdbb5dd35aa08ea9114436e0d79aceb2f38e32c21684dcf8e24e1e92821"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:92f93b21c0fe73dc00abf91022234c79d793318b8a96faac147cd579c1671746"},[m
[32m+[m[32m    {file = "mypy-1.10.0-cp39-cp39-win_amd64.whl", hash = "sha256:28d0e038361b45f099cc086d9dd99c15ff14d0188f44ac883010e172ce86c38a"},[m
[32m+[m[32m    {file = "mypy-1.10.0-py3-none-any.whl", hash = "sha256:f8c083976eb530019175aabadb60921e73b4f45736760826aa1689dda8208aee"},[m
[32m+[m[32m    {file = "mypy-1.10.0.tar.gz", hash = "sha256:3d087fcbec056c4ee34974da493a826ce316947485cef3901f511848e687c131"},[m
[32m+[m[32m][m
[32m+[m
[32m+[m[32m[package.dependencies][m
[32m+[m[32mmypy-extensions = ">=1.0.0"[m
[32m+[m[32mtyping-extensions = ">=4.1.0"[m
[32m+[m
[32m+[m[32m[package.extras][m
[32m+[m[32mdmypy = ["psutil (>=4.0)"][m
[32m+[m[32minstall-types = ["pip"][m
[32m+[m[32mmypyc = ["setuptools (>=50)"][m
[32m+[m[32mreports = ["lxml"][m
[32m+[m
[32m+[m[32m[[package]][m
[32m+[m[32mname = "mypy-extensions"[m
[32m+[m[32mversion = "1.0.0"[m
[32m+[m[32mdescription = "Type system extensions for programs checked with the mypy type checker."[m
[32m+[m[32moptional = false[m
[32m+[m[32mpython-versions = ">=3.5"[m
[32m+[m[32mfiles = [[m
[32m+[m[32m    {file = "mypy_extensions-1.0.0-py3-none-any.whl", hash = "sha256:4392f6c0eb8a5668a69e23d168ffa70f0be9ccfd32b5cc2d26a34ae5b844552d"},[m
[32m+[m[32m    {file = "mypy_extensions-1.0.0.tar.gz", hash = "sha256:75dbf8955dc00442a438fc4d0666508a9a97b6bd41aa2f0ffe9d2f2725af0782"},[m
[32m+[m[32m][m
[32m+[m
[32m+[m[32m[[package]][m
[32m+[m[32mname = "packaging"[m
[32m+[m[32mversion = "24.0"[m
[32m+[m[32mdescription = "Core utilities for Python packages"[m
[32m+[m[32moptional = false[m
[32m+[m[32mpython-versions = ">=3.7"[m
[32m+[m[32mfiles = [[m
[32m+[m[32m    {file = "packaging-24.0-py3-none-any.whl", hash = "sha256:2ddfb553fdf02fb784c234c7ba6ccc288296ceabec964ad2eae3777778130bc5"},[m
[32m+[m[32m    {file = "packaging-24.0.tar.gz", hash = "sha256:eb82c5e3e56209074766e6885bb04b8c38a0c015d0a30036ebe7ece34c9989e9"},[m
[32m+[m[32m