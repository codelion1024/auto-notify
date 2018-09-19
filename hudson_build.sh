#!/bin/bash

# body
# body
# body
# ...


OK_BUILD=`grep --quiet "Install system fs image: out/target/product/${PROJECT_NAME}/system.img" ${PROJECT_NAME}.log`
if [ $? != 0 ]; then
    echo -e "\e[31m ============================ build Failed ==================================== \e[0m"
    cd ${SCRIPT_DIR}
    ./hudson_auto_notify.py ${BUILD_URL} ${PROJECT_NAME} ${MANIFEST_BRANCH} ${HUDSON_BUILDs_ENV}/mydroid/android/qiku/ $JENKINS_URL
    exit 1
fi
