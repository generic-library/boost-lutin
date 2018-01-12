boost-lutin
===================

boost lutin wrapper


update new release

download the new vertion:
```
http://www.boost.org/users/history/
```

unzip in the boost path

==> request boost to generate all list of files:

```
cd boost
./bootstrap.sh
./b2 -a -n -j1 > ../build.txt
# update vertion in the next script:
./parseBuildOutputToLutin.py build.txt boost
```


