export ICE_HOME=/opt/ice-3.6.5-0.1.0
export PATH="$ICE_HOME/bin:$PATH"
#Remove commented out export below if Ice is not set globally accessible
export LD_LIBRARY_PATH="$ICE_HOME/lib64:$ICE_HOME/lib:$LD_LIBRARY_PATH"	
export SLICEPATH="$ICE_HOME/slice"
