#!/usr/local/bin/perl
# Save user and process options

use strict;
use warnings;
require 'virtualmin-nginx-lib.pl';
our (%text);
&lock_all_config_files();
my $parent = &get_config_parent();
my $events = &find("events", $parent);
&error_setup($text{'misc_err'});
&ReadParse();

&nginx_user_parse("user", $parent);

&nginx_opt_parse("worker_processes", $parent, undef, '^[1-9]\d*$');

&nginx_opt_parse("worker_priority", $parent, undef, '^\-?\d+$');

&flush_config_file_lines();
&unlock_all_config_files();
&webmin_log("misc");
&redirect("");
