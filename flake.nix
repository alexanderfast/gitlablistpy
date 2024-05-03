{
  description = "gitlablistpy";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        overlay = final: prev: {
          python39 = prev.python39.overrideAttrs (oldAttrs: {
            version = "3.9.6";
            src = final.fetchurl {
              url =
                "https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tar.xz";
              sha256 = "sha256-OXkgrzPvxbl/LgtX6RkjUS74n8WzwdIdv8jEgozgEIo=";
            };
          });
        };

        pkgs = import nixpkgs {
          inherit system;
          overlays = [ overlay ];
        };
      in {
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [ python39 poetry nixfmt ];
          shellHook = "";
        };
      });
}

