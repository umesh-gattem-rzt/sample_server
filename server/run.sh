#!/usr/bin/env bash


DEBUG=true
PYTHON_COMMAND=python3
PYTHON_PIP=pip3
PROJECT_NAME=sample_extension
PACKAGE_NAME=server
SCRIPT_PATH=`pwd`
python_exec_val=''
SCRIPT_NAME=$(basename "$0")
export PYTHONPATH=$PWD
CURRENT_DATE=`date +%d/%m/%Y`


python_snippet_init_cp=$"
import os
from fnmatch import fnmatch
from shutil import copyfile
pattern1='*__init__.py'
pattern2='*.json'
pattern3='*.yaml'
pattern4='*metadata.py'
# pattern5='*metadata.json'
def pattern_match(val):
 if fnmatch(val, pattern1):
    return True
 elif fnmatch(val, pattern2):
    return True
 elif fnmatch(val, pattern3):
    return True
 elif fnmatch(val, pattern4):
    return True
 return False
files = [val for val in
         [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk('./$PACKAGE_NAME')] for val in sublist] if pattern_match(val)]
[copyfile(file, '/tmp/$PROJECT_NAME'+file.replace('./','/')) for file in files]"



function generate_cython_dist(){
 : '
# @author: Prathyush SP
# @Created on: 21/05/17
# Description: Generate Cython Distribution
'
    rm -rf /tmp/${PROJECT_NAME}
    mkdir /tmp/${PROJECT_NAME}
    mkdir /tmp/${PROJECT_NAME}/${PACKAGE_NAME}
    cp -r * /tmp/${PROJECT_NAME}/${PACKAGE_NAME}
    cd /tmp/${PROJECT_NAME}/${PACKAGE_NAME}
    ${PYTHON_COMMAND} setup.py build_ext --inplace
    cd ${SCRIPT_PATH} &&  exec_python "$python_snippet_init_cp"
    cd /tmp/${PROJECT_NAME}/${PACKAGE_NAME}
    find . | grep -E "(__pycache__|\.pyc|\.pyo|\.py$)" | xargs rm -rf
    mkdir ${SCRIPT_PATH}/dist
    tar -cJvf ${SCRIPT_PATH}/dist/server-ct.tar.xz ./*
#    rm -rf ${tmp_dir}
}




case $1 in
"--cython") generate_cython_dist ;;
*) script_error ;;
esac