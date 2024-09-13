# MegaDownloader

## Installation and Usage 🚀

1. Visit [Lightning AI](https://lightning.ai/) 🌩️

2. Install on Linux:
   ```
   sudo apt install megatools
   ```

3. Run the script:
   ```
   python MegaDownloader.py
   ```

4. Paste the link to the file or folder you want to download.

## Manual 📚

For more information, check out these manuals:
- [Megatools Overview](https://manpages.ubuntu.com/manpages/focal/en/man7/megatools.7.html)
- [Megadl Command](https://manpages.ubuntu.com/manpages/focal/en/man1/megadl.1.html)

### For files:
```
megadl 'https://mega.nz/file/<some_id>#<some_other_id>' NOT OK
megadl 'https://mega.co.nz/#!<some_id>!<some_other_id>' OK
```
### For folder:
```
megadl 'https://mega.nz/file/<some_id>#<some_other_id>' NOT OK
megadl 'https://mega.co.nz/#F!<some_id>!<some_other_id>' OK
```


## WHY? 🤔

The download limit on Mega.nz is 5GB. By creating a new session in Lightning AI, you can continue downloading files when the limit is reached. Simply turn the virtual machine on and off to reset the limit.

If you know a better way to download files from Mega.nz without limits, or to resume downloading large files using megatools, please write in the issues!

