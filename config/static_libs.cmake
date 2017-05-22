
set(OPENJPEG_INCLUDE_DIR "/usr/include/" CACHE STRING "" FORCE)
set(OPENJPEG_LIBRARY "/usr/lib64/libopenjp2.a" CACHE STRING "" FORCE)

set(PNG_LIBRARY "/usr/lib64/libpng.a;m" CACHE STRING "" FORCE)

set(ZLIB_LIBRARY "/usr/lib64/libz.a" CACHE STRING "" FORCE)
set(TIFF_LIBRARY "/usr/lib64/libtiff.a" CACHE STRING "" FORCE)

set(JACK_LIBRARY "/usr/lib64/libjack.a" CACHE STRING "" FORCE)
set(JPEG_LIBRARY "/usr/lib64/libjpeg.a" CACHE STRING "" FORCE)
set(JEMALLOC_LIBRARY "/usr/lib64/libjemalloc.a" CACHE STRING "" FORCE)


set(OPENEXR_HALF_LIBRARY "/usr/lib64/libHalf.a" CACHE STRING "" FORCE)
set(OPENEXR_IEX_LIBRARY "/usr/lib64/libIex.a" CACHE STRING "" FORCE)
set(OPENEXR_ILMIMF_LIBRARY "/usr/lib64/libIlmImf.a" CACHE STRING "" FORCE)
set(OPENEXR_ILMTHREAD_LIBRARY "/usr/lib64/libIlmThread.a" CACHE STRING "" FORCE)
set(OPENEXR_IMATH_LIBRARY "/usr/lib64/libImath.a" CACHE STRING "" FORCE)

set(SNDFILE_LIBRARY
	/usr/lib64/libsndfile.a
	/usr/lib64/libFLAC.a
	/usr/lib64/libogg.a
	/usr/lib64/libvorbis.a
	/usr/lib64/libvorbisenc.a
	CACHE STRING "" FORCE)

set(FREETYPE_LIBRARY "/usr/lib64/libfreetype.a;/usr/lib64/libbz2.a" CACHE STRING "" FORCE)

set(FFMPEG_LIBRARIES
	/usr/lib64/libxvidcore.a
	/usr/lib64/libx264.a
	/usr/lib64/libmp3lame.a
	/usr/lib64/libvpx.a
	/usr/lib64/libvorbis.a
	/usr/lib64/libogg.a
	/usr/lib64/libvorbisenc.a
	/usr/lib64/libtheora.a
	/usr/lib64/libschroedinger-1.0.a
	/usr/lib64/liborc-0.4.a
	/usr/lib64/libavformat.a
	/usr/lib64/libavutil.a
	/usr/lib64/libavdevice.a
	/usr/lib64/libavcodec.a
	/usr/lib64/libavfilter.a
	/usr/lib64/libavresample.a
	/usr/lib64/libpostproc.a
	/usr/lib64/libswscale.a
	/usr/lib64/libswresample.a
	/usr/lib64/libv4l2.a
	/usr/lib64/libv4lconvert.a
	CACHE STRING "" FORCE)

set(OPENIMAGEIO_LIBRARY
	/usr/lib64/libOpenImageIO.a
	/usr/lib64/libpugixml.a
	/usr/lib64/libwebp.a
        /usr/lib64/libxvidcore.a
        /usr/lib64/libx264.a
        /usr/lib64/libmp3lame.a
        /usr/lib64/libvpx.a
        /usr/lib64/libvorbis.a
        /usr/lib64/libogg.a
        /usr/lib64/libvorbisenc.a
        /usr/lib64/libtheora.a
        /usr/lib64/libschroedinger-1.0.a
        /usr/lib64/liborc-0.4.a
        /usr/lib64/libavformat.a
        /usr/lib64/libavutil.a
        /usr/lib64/libavdevice.a
        /usr/lib64/libavcodec.a
        /usr/lib64/libavfilter.a
        /usr/lib64/libavresample.a
        /usr/lib64/libpostproc.a
        /usr/lib64/libswscale.a
        /usr/lib64/libswresample.a

	CACHE STRING "" FORCE)

set(OPENCOLORIO_OPENCOLORIO_LIBRARY
	/usr/lib64/libyaml.a
	/usr/lib64/libtinyxml.a
	/usr/lib64/libyaml-cpp.a
	/usr/lib64/libOpenColorIO.a
	CACHE STRING "" FORCE)

set(OPENCOLORIO_TINYXML_LIBRARY "/usr/lib64/libtinyxml.a" CACHE STRING "" FORCE)
set(OPENCOLORIO_YAML-CPP_LIBRARY "/usr/lib64/libyaml-cpp.a" CACHE STRING "" FORCE)

set(OPENCOLLADA_UTF_LIBRARY "/usr/lib64/opencollada/libUTF.a" CACHE STRING "" FORCE)

set(OPENAL_LIBRARY "/usr/lib64/libopenal.a" CACHE STRING "" FORCE)

set(PYTHON_LIBRARY "/usr/lib64/libpython3.5m.a" CACHE STRING "" FORCE)

set(TIFF_LIBRARY "/usr/lib64/libtiff.a" CACHE STRING "" FORCE)

set(SPACENAV_LIBRARY "/usr/lib64/libspnav.a" CACHE STRING "" FORCE)

set(OPENJPEG_LIBRARY "/usr/lib64/libopenjp2.a" CACHE STRING "" FORCE)
set(OPENJPEG_INCLUDE_DIR "/usr/include" CACHE STRING "" FORCE)

set(WITH_SDL_DYNLOAD ON CACHE BOOL "" FORCE)
set(LLVM_STATIC ON  CACHE BOOL "" FORCE)
set(WITH_OPENMP_STATIC ON  CACHE BOOL "" FORCE)

set(CMAKE_EXE_LINKER_FLAGS   "-lrt -static-libstdc++"  CACHE STRING "" FORCE)
