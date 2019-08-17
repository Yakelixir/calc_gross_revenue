
### Install

Notes:

Please make sure that you have python 3.6 or higher.
```sh
python --version
```

If this shows a 2.x version then please run... 

```sh
python3 --version
```

I have decided not to integrate asycnio or concurrent futures.
This in the essence of time and not knowing the demands of the application or its resources


Notes:
1. The following args are in a specific order that is not flexible currently
2. There are no installs needed or requirements as everything should come with a base python3 install
3. When using real files, we may have different permissions depending on the computer and operating system

### Usage

```sh
python yield_gross_rev.py <Product_File_Path> <Sales_File_Path> <Report_File_Name>
```