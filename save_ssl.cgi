#!/usr/local/bin/perl
# Save virtual host SSL options

use strict;
use warnings;
require 'virtualmin-nginx-lib.pl';
our (%text, %in);
&lock_all_config_files();
&error_setup($text{'ssl_err'});
&ReadParse();
my $server = &find_server($in{'id'});
$server || &error($text{'server_egone'});

&nginx_onoff_parse("ssl", $server);

# XXX
&nginx_opt_parse("ssl_certificate", $server, undef, \&valid_cert_file);

&nginx_opt_parse("ssl_certificate_key", $server, undef, \&valid_key_file);

if ($in{'ssl'} && $in{"ssl_certificate_def"}) {
	&error($text{'ssl_ecert'});
	}
if ($in{'ssl'} && (&valid_key_file("ssl_certificate") eq "" ||
		   (&valid_key_file("ssl_certificate_key") eq "")) {
	&error($text{'ssl_ekey'});
	}

&flush_config_file_lines();
&unlock_all_config_files();
my $name = &find_value("server_name", $server);
&webmin_log("ssl", "server", $name);
&redirect("edit_server.cgi?id=".&urlize($in{'id'}));

