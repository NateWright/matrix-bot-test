with import <nixpkgs> { };
stdenv.mkDerivation rec {
  name = "jupyter";
  env = buildEnv { name = name; paths = buildInputs; };
  buildInputs = with python311Packages; [
    matrix-nio
  ];
}

