#!/bin/sh
UE4_TRUE_SCRIPT_NAME=$(echo \"$0\" | xargs readlink -f)
UE4_PROJECT_ROOT=$(dirname "$UE4_TRUE_SCRIPT_NAME")
chmod +x "$UE4_PROJECT_ROOT/Engine/Binaries/Linux/UE4Game-Linux-Shipping"
"$UE4_PROJECT_ROOT/Engine/Binaries/Linux/UE4Game-Linux-Shipping" \"../../../BasilicaSudak_UE4/BasilicaSudak_UE4.uproject\" $@ 
