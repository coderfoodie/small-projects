<?php
    // first forwarded IP match it finds
    function forwarded_ip() {
        // making fake IPs
        // $server = array(
        //     'HTTP_X_FORWARDED_FOR' => '1.1.1.1',
        //     'HTTP_X_FORWARDED' => '2.2.2.2'
        // );
        $keys = array(
            'HTTP_X_FORWARDED_FOR',
            'HTTP_X_FORWARDED',
            'HTTP_FORWARDED_FOR',
            'HTTP_FORWARDED',
            'HTTP_CLIENT_IP',
            'HTTP_X_CLUSTER_CLIENT_IP'
        );

        foreach ($keys as $key) {
            if (isset($_SERVER[$key])) {
                $ip_array = explode(',', $_SERVER[$key]);
                foreach ($ip_array as $ip) {
                    $ip = trim($ip);
                    return $ip;
                }
            }
        }
        return '';
    }
    // $remote_ip = $_SERVER['REMOTE_ADDR']; //fake server
    
    $forwarded_ip = forwarded_ip();
?>

<h3>Remote IP Address: <? echo $remote_ip; ?></h3>
<br><br>
<?php if ($forwarded_ip != '') { ?>
    Forwarded for: <? echo $forwarded_ip; ?> 
<?php } ?>
<h3></h3>