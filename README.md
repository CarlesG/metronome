# CLI METROTRONOME

CLI metronome. To install dependencies use:

```
pip install -r requirements.txt
```

or with conda:

```
conda create --name myenv --file requirements.txt
```

Example of use in CLI: 

```
python metronome.py 120 --vol 0.5
python metronome.py 60
```

options
-h          : shows the help
--vol option: fix the volume to a value (default:13)

To execute in the background at windows:

``` start python metronome.py 120 ```
