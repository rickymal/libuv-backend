{ pkgs ? import <nixpkgs> {} }:

let
  tomlExample = {
    title = "TOML Example";

    owner = {
      name = "Tom Preston-Werner";
      dob = "1979-05-27T07:32:00-08:00";
    };

    database = {
      enabled = true;
      ports = [ 8000 8001 8002 ];
      data = [ ["delta" "phi"] [3.14] ];
      temp_targets = {
        cpu = 79.5;
        case = 72.0;
      };
    };

    servers = {
      alpha = {
        ip = "10.0.0.1";
        dc = "eqdc10";
      };
      beta = {
        ip = "10.0.0.2";
        dc = "eqdc10";
        country = "中国";
      };
    };

    clients = {
      hosts = [ "alpha" "omega" ];
    };

    products = {
      gadget = [
        {
          name = "Foobar Elite";
          sku = 732895;
          color = "black";
        }
        {
          name = "Foobar Deluxe";
          sku = 732896;
          color = "white";
        }
      ];
    };

    fruit = {
      apple = {
        color = "red";
        taste.sweet = true;
        texture.smooth = true;
      };
    };

    points = [
      { x = 1; y = 2; z = 3; }
      { x = 7; y = 8; z = 9; }
      { x = 2; y = 4; z = 8; }
    ];

    strings = {
      str1 = "I'm a string.";
      str2 = ''
        I'm a multiline
        string.'';
    };

    integers = {
      int1 = 99;
      int2 = 42;
      int3 = 0;
      int4 = -17;
    };

    floats = {
      flt1 = 1.0;
      flt2 = 3.1415;
      flt3 = -0.01;
    };

    booleans = {
      bool1 = true;
      bool2 = false;
    };

    datetime = {
      date1 = "1979-05-27T07:32:00Z";
      date2 = "1979-05-27T00:32:00-07:00";
      date3 = "1979-05-27T00:32:00.999999-07:00";
    };

    array_of_tables = {
      product = [
        {
          name = "Hammer";
          sku = 738594937;
        }
        {
          name = "Nail";
          sku = 284758393;
          color = "gray";
        }
      ];
    };
  };

in pkgs.stdenv.mkDerivation {
  name = "toml-example";
  
  buildInputs = [ pkgs.jq ];

  buildPhase = ''
    echo '${builtins.toJSON tomlExample}' | jq '.' > toml_example.json
  '';

  installPhase = ''
    mkdir -p $out/share
    cp toml_example.json $out/share/
  '';

  meta = {
    description = "A Nix representation of the TOML example";
    license = pkgs.lib.licenses.mit;
  };
}
