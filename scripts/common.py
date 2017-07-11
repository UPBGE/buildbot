homeDir = "/home/tristan/"

prefixSourceDir = homeDir + "source/"
blenderSourceDir = prefixSourceDir + "blender/"

traceMainScript = homeDir + "scripts/mainloop/TraceMain.py"
traceDir = homeDir + "trace/"
imageDir = homeDir + "image/"

docDir = prefixSourceDir + "doc/"

configDir = homeDir + "config/"

doxygenDir = docDir + "doc/doxygen/"
doxygenBuildDir = doxygenDir + "html/"
doxygenConfigFile = configDir + "doxygen/Doxyfile"

sphinxDir = docDir + "doc/python_api/"
sphinxScript = sphinxDir + "sphinx_doc_gen.py"
sphinxInputDir = sphinxDir + "sphinx-in/"
sphinxOutputDir = sphinxDir + "sphinx-out/"

logDir = homeDir + "logs/"
buildLogDir = logDir + "build/"
testLogDir = logDir + "test/"
valgrindLogDir = testLogDir + "valgrind/"
pythonTestLogDir = testLogDir + "python/"

valgrindSuppressionsFile = configDir + "valgrind-suppressions.supp"

testFiles = homeDir + "files/"
pythonMainScript = homeDir + "scripts/mainloop/"

prefixBuildBranchDir = homeDir + "build_normal/"
prefixBuildBranchDebugDir = homeDir + "build_debug/"
prefixBuildReleaseDir = homeDir + "build_release/"
prefixBuildDebugDir = homeDir + "build_debug/"

releaseConfigFile = configDir + "release_make_config.cmake"
liteConfigFile = configDir + "branch_make_config.cmake"
debugConfigFile = configDir + "debug_make_config.cmake"

libsListFile = configDir + "libs.txt"

hashDir = homeDir + "build_hash/"
branchHashDir = hashDir + "branch/"
releaseHashDir = hashDir + "release/"
releaseHashDir = hashDir + "debug/"
branchMaskFile = configDir + "branch.mask"

releaseDir = homeDir + "releases/"
linuxReleaseDir = homeDir + "download/release/linux64/"
linuxBranchDir = homeDir + "download/buildbot/branch/"

printVersionFile = homeDir + "version.txt"
printVersionBlendFile = homeDir + "print_version.blend"

compileProcess = 4
