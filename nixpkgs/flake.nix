{
  inputs = {
    unstable.url = "github:NixOS/nixpkgs/nixos-unstable";
    "24.11".url = "github:NixOS/nixpkgs/nixos-24.11";
  };
  outputs = inputs: inputs;
}
