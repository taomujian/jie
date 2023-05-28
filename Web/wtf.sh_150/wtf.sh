$ source user_functions.sh
<head>
    <link rel="stylesheet" type="text/css" href="/css/std.css" >
</head>
<body>
    <h1>Welcome to the wtf.sh Forums!</h1>
$ if is_logged_in
$ then
$   echo "<p>Hi, ${COOKIES['USERNAME']}. <a href='/logout.wtf'>Logout</a> <a href='/profile.wtf?user=$(basename $(find_user_file ${COOKIES['USERNAME']}))'>Profile</a></p>"
$   echo "<a href=/new_post.wtf>New Post</a>";
$ else
$   echo "<p>You're not logged in. <a href='/login.wtf'>Login</a> <a href='/new_user.wtf'>Register</a></p>"
$ fi
    <h3>Posts:</h3>
    <ol>
$ if [[ -e .index_cache.html ]]
$ then
$   cat .index_cache.html;
$ else
$   for post_file in posts/*; do
$       post_file=$(basename $post_file);
$       post_title=$(nth_line 2 < posts/$post_file | htmlentities);
$       post_user=$(nth_line 1 < posts/$post_file | htmlentities);
$       echo "<li><a href=\"/post.wtf?post=$post_file\">$post_title</a> by ${post_user}</li>";
$   done;
$ fi
    </ol>
</body>
</html></span>
</div>
<div class="post">
<span class="post-poster">Posted by <a href="/profile.wtf?user=NONE">#!/usr/bin/env bash</a></span>
<span class="post-title"></span>
<span class="post-body"># Some useful standard functions to have around :)

# check if an array contains a given value
# contains "asdf" "asdf an array of values" => has exit code 0
function contains {
    local e;
    for e in "${@:2}"; do [[ "$e" == "$1" ]] && return 0; done;
    return 1;
}

function file_exists {
    local file=$1;
    stat ${file} > /dev/null;
}

function nth_line {
    local n=$1;
    local filename;
    if [[ $# != 1 ]]
    then
        filename=$2;
        sed "${n}q;d" < $filename;
    else
        sed "${n}q;d"
    fi 2> /dev/null
}

function redirect {
    local target="$1";
    echo "<script>window.location.href='${target}';</script>";
}

# Hacky way of figuring out which date command is appropriate,
# depending if we're on BSD or GNU coreutils
YESTERDAY_CMD="";
TOMORROW_CMD="";
if date --help | grep "GNU" > /dev/null
then
    # Using GNU date
    TOMORROW_CMD="date -d tomorrow";
    YESTERDAY_CMD="date -d yesterday";
else
    # Using BSD date
    TOMORROW_CMD="date -v +1d";
    YESTERDAY_CMD="date -v -1d";
fi

function set_cookie {
    local key="$1";
    local value="$2";
    local expiry=$(${TOMORROW_CMD});
    echo "<script>document.cookie = '${key}=${value}; expires=${expiry}; path=/';</script>";
    COOKIES[$key]="${value}";
}

function get_cookie {
    echo "${COOKIES[$1]}";
}

function remove_cookie {
    local key="$1";
    local expiry=$(${YESTERDAY_CMD}); # expiration dates in the past delete cookies
    echo "<script>document.cookie = '${key}=riperino; expires=${expiry}; path=/';</script>";
    unset COOKIES[$key];
}

# take text on input, transform any html special chars to the corresponding entities
function htmlentities {
    sed "s/\&/\&/g" | sed "s/</\&lt;/g" | sed "s/>/\&gt;/g";
}</span>
</div>
<div class="post">
<span class="post-poster">Posted by <a href="/profile.wtf?user=NONE">$ # vim: ft=wtf</a></span>
<span class="post-title"><html></span>
<span class="post-body"><head>
    <link rel="stylesheet" type="text/css" href="/css/std.css" >
</head>
$ source user_functions.sh
$ if [[ $method = 'POST' ]]
$ then
$   local username=${POST_PARAMS['username']};
$   local password=${POST_PARAMS['password']};
$   local userfile=$(find_user_file ${username});
$   if [[ ${userfile} != 'NONE' ]]
$   then 
$       # User exists, try to login
$       if $(check_password ${username} ${password})
$       then
$           # correct pass
$           set_cookie "USERNAME" ${username};
$           set_cookie "TOKEN" $(nth_line 3 ${userfile});
$           redirect "/";
$       else 
$           # incorrect pass
$           echo "<h3>Sorry, wrong password for user ${username}:(<br>Try again?</h3>";
$       fi
$   else
$       # user doesn't exist
$       echo "<h3>Sorry, user ${username} doesn't exist :(<br>Try again?</h3>"
$   fi
$ fi
<h3>Login</h3>
<form method=POST>
<input type=text name=username placeholder="username"></input><br>
<input type=password name=password placeholder="password"></input><br>
<button type=submit name=submit>Submit</button>
</form>
</html></span>
</div>
<div class="post">
<span class="post-poster">Posted by <a href="/profile.wtf?user=NONE">$ # vim: ft=wtf</a></span>
<span class="post-title"><html></span>
<span class="post-body"><head>
    <link rel="stylesheet" type="text/css" href="/css/std.css" >
</head>
$ source user_functions.sh
$ if is_logged_in
$ then 
$   remove_cookie 'USERNAME';
$   remove_cookie 'TOKEN';
$   redirect "/";
$ else
$   echo "<h3>You need to be logged in to log out, bud.</h3>";
$ fi
</html></span>
</div>
<div class="post">
<span class="post-poster">Posted by <a href="/profile.wtf?user=NONE">$ # vim: ft=wtf</a></span>
<span class="post-title"><html></span>
<span class="post-body"><head>
    <link rel="stylesheet" type="text/css" href="/css/std.css" >
</head>
$ source user_functions.sh
$ source post_functions.sh
$ if [[ $method = 'POST' ]]
$ then
$   if is_logged_in
$   then
$       post_id=$(create_post "${COOKIES['USERNAME']}" "${POST_PARAMS['title']}" "${POST_PARAMS['text']}");
$       redirect "/post.wtf?post=${post_id}";
$   else
$       echo "<h3>pls login 2 be posting</h3>";
$   fi
$ fi
<form method=POST>
<input type=text name=title placeholder="Post Title"></input><br>
<textarea name=text placeholder="Post Text"></textarea><br>
<button type=submit name=submit>Submit</button>
</form>
</html></span>
</div>
<div class="post">
<span class="post-poster">Posted by <a href="/profile.wtf?user=NONE">$ # vim: ft=wtf</a></span>
<span class="post-title"><html></span>
<span class="post-body"><head>
    <link rel="stylesheet" type="text/css" href="/css/std.css" >
</head>
$ source user_functions.sh
$ if [[ $method = 'POST' ]]
$ then
$   local username=${POST_PARAMS['username']};
$   local password=${POST_PARAMS['password']};
$   if [[ $(find_user_file "${username}") = 'NONE' ]]
$   then 
$       # create user
$       echo "ok, gonna go make that user... ${username}";
$       local user_id=$(create_user "${username}" "${password}");
$       redirect "/login.wtf";
$   else
$       # user already exists
$       echo "<h3>Sorry, user ${username} already exists :(<br>Try again?</h3>"
$   fi
$ fi
<h3>Register</h3>
<form method=POST>
<input type=text name=username placeholder="username"></input><br>
<input type=password name=password placeholder="password"></input><br>
<button type=submit name=submit>Submit</button>
</form>
</html></span>
</div>
<div class="post">
<span class="post-poster">Posted by <a href="/profile.wtf?user=NONE">$ # vim: ft=wtf</a></span>
<span class="post-title"><html></span>
<span class="post-body"><head>
    <link rel="stylesheet" type="text/css" href="/css/std.css" >
    <link rel="stylesheet" type="text/css" href="/css/post.css" >
</head>
<body>
$ source user_functions.sh
$ if contains 'post' ${!URL_PARAMS[@]} && file_exists "posts/${URL_PARAMS['post']}"
$ then
$   post_id=${URL_PARAMS['post']};
$   for post_file in $(ls posts/${post_id}/* | sort --field-separator='/' --key=3 -n); do
$       echo "<div class=\"post\">";
$       poster=$(nth_line 1 ${post_file} | htmlentities);
$       title=$(nth_line 2 ${post_file} | htmlentities);
$       body=$(tail -n +3 ${post_file} | htmlentities 2> /dev/null);
$       echo "<span class=\"post-poster\">Posted by <a href=\"/profile.wtf?user=$(basename $(find_user_file "${poster}"))\">${poster}</a></span>";
$       echo "<span class=\"post-title\">$title</span>";
$       echo "<span class=\"post-body\">$body</span>";
$       echo "</div>";
$   done
$ else
$   echo "Pls give a (valid) post id";
$ fi;

<div class="action-btns">
$   echo "<a href=\"/reply.wtf?post=${post_id}\">Reply</a>"
<a href="/">Back</a>
</div>

</body>
</html></span>
</div>
<div class="post">
<span class="post-poster">Posted by <a href="/profile.wtf?user=NONE">#!/usr/bin/env bash</a></span>
<span class="post-title"></span>
<span class="post-body">source user_functions.sh

# Create a new post. Returns the post id.
function create_post {
    local username=$1;
    local title=$2;
    local text=$3;
    local hashed=$(hash_username "${username}");

    # ensure posts dir exists and isn't listable.
    mkdir posts 2> /dev/null;
    touch posts/.nolist; # don't allow directory listing on posts
    touch posts/.noread; # don't allow file reads on post

    local post_id=$(basename $(mktemp --directory posts/XXXXX));


    echo ${username} > "posts/${post_id}/1";
    echo ${title} >> "posts/${post_id}/1";
    echo ${text} >> "posts/${post_id}/1";

    touch "posts/${post_id}/.nolist";
    touch "posts/${post_id}/.noread";


    # add to our cache for the homepage
    echo "<li><a href=\"/post.wtf?post=${post_id}\">$(htmlentities <<< ${title})</a> by $(htmlentities <<< ${username})</li>" >> .index_cache.html

    # add post to users' post cache
    local hashed=$(hash_username "${username}");
    echo "${post_id}/1" >> "users_lookup/${hashed}/posts";

    echo ${post_id};

}

function reply {
    local post_id=$1;
    local username=$2;
    local text=$3;
    local hashed=$(hash_username "${username}");

    curr_id=$(for d in posts/${post_id}/*; do basename $d; done | sort -n | tail -n 1);
    next_reply_id=$(awk '{print $1+1}' <<< "${curr_id}");
    next_file=(posts/${post_id}/${next_reply_id});
    echo "${username}" > "${next_file}";
    echo "RE: $(nth_line 2 < "posts/${post_id}/1")" >> "${next_file}";
    echo "${text}" >> "${next_file}";

    # add post this is in reply to to posts cache
    echo "${post_id}/${next_reply_id}" >> "users_lookup/${hashed}/posts";
}</span>
</div>
<div class="post">
<span class="post-poster">Posted by <a href="/profile.wtf?user=NONE"></a></span>
<span class="post-title"></span>
<span class="post-body"></span>
</div>
<div class="post">
<span class="post-poster">Posted by <a href="/profile.wtf?user=NONE">$ # vim: ft=wtf</a></span>
<span class="post-title">$ source user_functions.sh</span>
<span class="post-body"><html>
<head>
    <link rel="stylesheet" type="text/css" href="/css/std.css" >
</head>
$ if contains 'user' ${!URL_PARAMS[@]} && file_exists "users/${URL_PARAMS['user']}"
$ then
$   local username=$(head -n 1 users/${URL_PARAMS['user']});
$   echo "<h3>${username}'s posts:</h3>";
$   echo "<ol>";
$   get_users_posts "${username}" | while read -r post; do
$       post_slug=$(awk -F/ '{print $2 "#" $3}' <<< "${post}");
$       echo "<li><a href=\"/post.wtf?post=${post_slug}\">$(nth_line 2 "${post}" | htmlentities)</a></li>";
$   done 
$   echo "</ol>";
$   if is_logged_in && [[ "${COOKIES['USERNAME']}" = 'admin' ]] && [[ ${username} = 'admin' ]]
$   then
$       get_flag1
$   fi
$ fi
</html></span>
</div>
<div class="post">
<span class="post-poster">Posted by <a href="/profile.wtf?user=NONE">$ # vim: ft=wtf</a></span>
<span class="post-title"><html></span>
<span class="post-body"><head>
    <link rel="stylesheet" type="text/css" href="/css/std.css" >
</head>
$ source user_functions.sh
$ source post_functions.sh
$ if [[ $method = 'POST' ]]
$ then
$   if is_logged_in
$   then
$       if [[ ${POST_PARAMS['text']} != '' && ${URL_PARAMS['post']} != '' ]]
$       then
$           reply "${URL_PARAMS['post']}" "${COOKIES['USERNAME']}" "${POST_PARAMS['text']}"
$           redirect "/post.wtf?post=${URL_PARAMS['post']}#${next_post_id}";
$       else
$           redirect "/reply.wtf?post=${URL_PARAMS['post']}";
$       fi
$   else
$      redirect "/login.wtf"
$   fi
$ fi

$ if [[ ${URL_PARAMS['post']} = '' ]] 
$ then
$   echo "u need to be replying to a post, you dumdum";
$ fi

$ if is_logged_in
$ then
$   echo "u r logged in, s0 gib reply"
$ else
$   redirect "/login.wtf"
$ fi
<form method=POST>
<textarea name=text placeholder="Reply Text"></textarea><br>
<button type=submit name=submit>Submit</button>
</form>
</html></span>
</div>
<div class="post">
<span class="post-poster">Posted by <a href="/profile.wtf?user=NONE">#!/usr/bin/env bash</a></span>
<span class="post-title"></span>
<span class="post-body">cp -R /opt/wtf.sh /tmp/wtf_runtime;

# protect our stuff
chmod -R 555 /tmp/wtf_runtime/wtf.sh/*.wtf;
chmod -R 555 /tmp/wtf_runtime/wtf.sh/*.sh;
chmod 777 /tmp/wtf_runtime/wtf.sh/;

# set all dirs we could want to write into to be owned by www
# (We don't do whole webroot since we want the people to be able to create
#   files in webroot, but not overwrite existing files)
chmod -R 777 /tmp/wtf_runtime/wtf.sh/posts/;
chown -R www:www /tmp/wtf_runtime/wtf.sh/posts/;

chmod -R 777 /tmp/wtf_runtime/wtf.sh/users/;
chown -R www:www /tmp/wtf_runtime/wtf.sh/users/;

chmod -R 777 /tmp/wtf_runtime/wtf.sh/users_lookup/;
chown -R www:www /tmp/wtf_runtime/wtf.sh/users_lookup/;

# let's get this party started!
su www -c "/tmp/wtf_runtime/wtf.sh/wtf.sh 8000";</span>
</div>
<div class="post">
<span class="post-poster">Posted by <a href="/profile.wtf?user=NONE">#!/usr/local/bin/bash</a></span>
<span class="post-title"></span>
<span class="post-body">function hash_password {
    local password=$1;
    (shasum <<< ${password}) | cut -d\  -f1;
}

# hash usernames for lookup in the users_lookup table
function hash_username {
    local username=$1;
    (shasum <<< ${username}) | cut -d\  -f1;
}

# generate a random token, base64 encoded
# on GNU base64 wraps at 76 characters, so we need to pass --wrap=0
function generate_token {
    (head -c 64 | (base64 --wrap=0 || base64)) < /dev/urandom 2> /dev/null;
}

function find_user_file {
    local username=$1;
    local hashed=$(hash_username "${username}");
    local f;
    if [[ -n "${username}" && -e "users_lookup/${hashed}" ]]
    then
        echo "users/$(cat "users_lookup/${hashed}/userid")";
    else
        echo "NONE"; # our failure case -- ugly but w/e...
    fi;
    return;
}

# The caller is responsible for checking that the user doesn't exist already calling this
function create_user {
    local username=$1;
    local password=$2;
    local hashed_pass=$(hash_password ${password});
    local hashed_username=$(hash_username "${username}");
    local token=$(generate_token);

    mkdir users 2> /dev/null; # make sure users directory exists
    touch users/.nolist; # make sure that the users dir can't be listed
    touch users/.noread; # don't allow reading of user files directly

    mkdir users_lookup 2> /dev/null; # make sure the username -> userid lookup directory exists
    touch users_lookup/.nolist; # don't let it be listed

    local user_id=$(basename $(mktemp users/XXXXX));


    # user files look like:
    #   username
    #   hashed_pass
    #   token
    echo "${username}" > "users/${user_id}";
    echo "${hashed_pass}" >> "users/${user_id}";
    echo "${token}" >> "users/${user_id}";


    mkdir "users_lookup/${hashed_username}" 2> /dev/null;
    touch "users_lookup/${hashed_username}/.nolist"; # lookup dir for this user can't be readable
    touch "users_lookup/${hashed_username}/.noread"; # don't allow reading the lookup dir
    touch "users_lookup/${hashed_username}/posts"; # lookup for posts this user has participated in
    echo "${user_id}" > "users_lookup/${hashed_username}/userid"; # create reverse lookup

    echo ${user_id};
}

function check_password {
    local username=$1;
    local password=$2;
    local userfile=$(find_user_file ${username});

    if [[ ${userfile} = 'NONE' ]]
    then
        return 1;
    fi

    local hashed_pass=$(hash_password ${password});
    local correct_hash=$(head -n2 ${userfile} | tail -n1);
    [[ ${hashed_pass} = ${correct_hash} ]];
    return $?;
}

function is_logged_in {
    contains 'TOKEN' ${!COOKIES[@]} && contains 'USERNAME' ${!COOKIES[@]};
    local has_cookies=$?
    local userfile=$(find_user_file ${COOKIES['USERNAME']});
    [[ ${has_cookies} \
        && ${userfile} != 'NONE' \
        && $(tail -n1 ${userfile} 2>/dev/null) = ${COOKIES['TOKEN']} \
        && $(head -n1 ${userfile} 2>/dev/null) = ${COOKIES['USERNAME']} \
    ]];
    return $?;
}

function get_users_posts {
    local username=$1;
    local hashed=$(hash_username "${username}");
    # we only have to iterate over posts a user has replied to
    while read -r post_id; do
        echo "posts/${post_id}";
    done < "users_lookup/${hashed}/posts";
}</span>
</div>
<div class="post">
<span class="post-poster">Posted by <a href="/profile.wtf?user=NONE"></a></span>
<span class="post-title"></span>
<span class="post-body"></span>
</div>
<div class="post">
<span class="post-poster">Posted by <a href="/profile.wtf?user=NONE"></a></span>
<span class="post-title"></span>
<span class="post-body"></span>
</div>
<div class="post">
<span class="post-poster">Posted by <a href="/profile.wtf?user=NONE">#!/usr/bin/env bash</a></span>
<span class="post-title"></span>
<span class="post-body"># config stuff
PROCESS_LIMIT=512 # per connection
PROFILE=false

# shell options
shopt -s extglob;

# ~~ PROFILING ~~
if [[ $PROFILE = true ]]
then
    PS4='+ $(date "+%s.%N") $(if [[ ${FUNCNAME} = "" ]]; then echo NONE; else echo "${FUNCNAME}"; fi ) ${LINENO}\011 '
    exec 3>&2 2>/tmp/bashprof.$$.log
    set -x
fi

# sick facts about bash
declare -a BASH_FACTS=(
    $'Bash has an `until` keyword, which is equivalent to `while not`.' 
    $'Single and Double quotes do different things in bash -- single quotes do not interpolate variables, while double quotes do.' 
    $'When globbing on arrays in bash, you have the option to use [*] and [@], which appear to both return all the elements of the array. However, [*] acts like a "splat operator", while [@] keeps all everything constrained to the same argument.' 
    $'The bash array access syntax looks like ${array[$idx]}.' 
    $'If you forget the brackets in an array access, bash will just return the first element of the array.' 
    $'Bash didn\'t have Associative Arrays until Bash 4' 
    $'The idomatic way of iterating over all the lines in a file in bash is `while read -r line; do <something with line>; done < <filename>`' 
    $'Loops are just commands. So, you can pipe things into and out of them!'
    );

source lib.sh # import stdlib

VERSION="0.0.0.0.1 \"alphaest of bets\""
declare -a REPLY_HEADERS=(
    "X-Powered-By: wtf.sh ${VERSION}" # Fly the banner of wtf.sh proudly!
    "X-Bash-Fact: $(shuf --head-count=1 -e "${BASH_FACTS[@]}")" # select a random BASH FACT to include
);

declare -A URL_PARAMS # hashtable of url parameters
declare -A POST_PARAMS # hashtable of post parameters
declare -A HTTP_HEADERS # hashtable of http headers
declare -A COOKIES # hashtable of cookies



function log {
    echo "[`date`] $@" 1>&9
}

urldecode() {
    # urldecode <string>

    local url_encoded="${1//+/ }"
    printf '%b' "${url_encoded//%/\\x}"
}

max_page_include_depth=64
page_include_depth=0
function include_page {
    # include_page <pathname>
    local pathname=$1
    local cmd=""
    [[ "${pathname:(-4)}" = '.wtf' ]];
    local can_execute=$?;
    page_include_depth=$(($page_include_depth+1))
    if [[ $page_include_depth -lt $max_page_include_depth ]]
    then
        local line;
        while read -r line; do
            # check if we're in a script line or not ($ at the beginning implies script line)
            # also, our extension needs to be .wtf
            [[ "$" = "${line:0:1}" && ${can_execute} = 0 ]];
            is_script=$?;

            # execute the line.
            if [[ $is_script = 0 ]]
            then
                cmd+=$'\n'"${line#"$"}";
            else
                if [[ -n $cmd ]]
                then
                    eval "$cmd" || log "Error during execution of ${cmd}";
                    cmd=""
                fi
                echo $line
            fi
        done < ${pathname}
    else
        echo "<p>Max include depth exceeded!<p>"
    fi
}

function parse_headers {
    while read -r line; do
        if [[ $line = $'\r' || $line == $'\n' ]]
        then
            break
        else
            a=($line)
            key=${a[0]%?}
            value=${a[@]:1}
            HTTP_HEADERS[$key]=${value:0:-1}; # remove \r from end
        fi
    done
}

function parse_cookies {
    while read -d ';' -r cookie; do
        local key=$(cut -d\= -f1 <<< "${cookie}");
        local value=${cookie#*=};
        COOKIES[${key}]=${value};
    done <<< "${HTTP_HEADERS['Cookie']};" # append a ; so we still get the last field -- read drops the last thing >_<
}

function handle_connection {
    ulimit -u "${PROCESS_LIMIT}"; # limit num processes per connection

    # Parse query and any url parameters that may be in the path
    IFS=' ' read -r method path version

    # fast fail on empty request
    if [[ ${method} = '' ]]
    then
        return
    fi

    query=${path##*\?};
    if [[ $query != $path ]]
    then
        while read -d '&' -r param; do
            IFS='=' read key value <<< ${param};
            URL_PARAMS[$key]=$(urldecode $value)
        done <<< "${query}&" # add & so last argument is seen
    fi

    request=("$method" "$path" "$version")
    path=$(urldecode $(cut -d\? -f1 <<< "${path}")) # strip url parameters, urldecode

    # parse headers
    parse_headers;

    # parse out cookie values, if they exist
    if contains "Cookie" "${!HTTP_HEADERS[@]}"
    then
        parse_cookies;
    fi
    
    if [[ $method == "POST" ]]
    then
        # TODO: handle multipart bodies
        local line;
        local n;
        n=${HTTP_HEADERS['Content-Length']};
        read -n$n -r line;
        params=($(sed "s/\&/ /g" <<< "${line}"))
        for param in ${params[@]}; do
            IFS='=' read key value <<< ${param};
            POST_PARAMS[$key]=$(urldecode $value)
        done
    fi

    # if we know the IP (via an X-Forwarded-For header), stick the user in a sandbox
    # (Cloudflare will fill in this IP in prod, we can also have nginx fill it in in dev if we want)
    if contains "X-Forwarded-For" "${!HTTP_HEADERS[@]}"
    then
        sandbox_dir="$((cksum <<< ${HTTP_HEADERS["X-Forwarded-For"]}) | cut -d\  -f1).sandbox";
        # create sandbox if it doesn't exist
        if [[ ! -e "${sandbox_dir}" ]]
        then
            mkdir "${sandbox_dir}";
            # copy anything that isn't itself a sandbox to the dir
            cp -R !(*.sandbox) "${sandbox_dir}";
        fi
        cd "${sandbox_dir}";
    else
        log "WARNING: Not sandboxing: no X-Forwarded-For header found!"
    fi

    requested_path=$(pwd)/${path}

    # if a directory is requested, try each of the following, in order
    # index.wtf, index.html
    local index_fills=("index.wtf" "index.html");
    if [[ -d ${requested_path} ]]
    then
        for i in ${index_fills}; do
            if [[ -e "${requested_path}/${i}" ]]
            then
                requested_path="${requested_path}/${i}";
                break;
            fi
        done
    fi

    # check for possible directory traversals / other undesirable path elements by
    # removing them and 503-ing if the string was changed
    test_path=$(sed "s/\.\.//g" <<< "${requested_path}")
    if [[ ${test_path} != ${requested_path} ]]
    then
        echo "HTTP/1.1 503 Forbidden"
        echo "Content-Type: text/html"
        for reply_header in "${REPLY_HEADERS[@]}"; do
            echo "${reply_header}"
        done
        printf "\r\n\r\n"
        echo "<html><title>503</title><body>503 Forbidden</body></html>"
        echo "<p>Sorry, directory traversal is strongly frowned upon here at wtf.sh enterprises</p>";
        log "503: ${request[@]}"
        exit 0; # terminate early for 503
    fi

    [[ ! -e "${requested_path}/.nolist" ]];
    local can_list=$?;
    [[ ! -e "$(dirname "${requested_path}")/.noread" ]];
    local can_read=$?;

    if [[ -e ${requested_path}  ]]
    then
        if [[ -f ${requested_path} \
            && ${requested_path:(-4)} != ".log"\
            && ${can_read} = 0 ]] # can't end in .log, can't have .noread in the parent directory
        then
            echo "HTTP/1.1 200 OK"
            echo "Content-Type: text/html"
            for reply_header in "${REPLY_HEADERS[@]}"; do
                echo "${reply_header}"
            done
            printf "\r\n\r\n"
            include_page ${requested_path};
        elif [[ -d ${requested_path} \
            && ${can_list} = 0 ]] # handle directory listing if it isn't a file and no `.nolist` file in the directory
        then
            log "$(dirname "${requested_path}")/.noread"
            echo "HTTP/1.1 200 OK"
            echo "Content-Type: text/html"
            for reply_header in "${REPLY_HEADERS[@]}"; do
                echo "${reply_header}"
            done
            printf "\r\n\r\n"
            echo "<h3>Index of ${request[1]}</h3>"
            echo "<ul>"
            for d in ${requested_path}/*; do
                size_info=($(du -h ${requested_path} | tail -n 1))
                echo "<li><a href="/${request[1]#"/"}${d}">${d}</a>: ${size_info[0]}</li>"
            done
            echo "</ul>"
            echo "<font size=2>generated by wtf.sh ${VERSION} on $(date)</font>"
        else
            echo "HTTP/1.1 503 Forbidden"
            echo "Content-Type: text/html"
            for reply_header in "${REPLY_HEADERS[@]}"; do
                echo "${reply_header}"
            done
            printf "\r\n\r\n"
            echo "<title>503 Forbidden</title>";
            echo "<h3>I'm sorry, I'm afraid I can't let you see that</h3>";
            echo "<p>It seems that you tried to list a directory with a <code>.nolist</code> file in it, or a <code>.noread</code> file in it's parent, or a forbidden file type.</p>";
            echo "<p>If you think this was a mistake, I feel bad for you, son. I got 99 problems, but a 503 ain't one.</p>";
            log "503: ${request[@]}"
            exit 0;
        fi
        log "200: ${request[@]}"
        exit 0
    else
        # If we were noread or nolist, send a 503, even though the resource doesn't even exist -- we don't want to leak what forbidden resources do and do not exist
        if [[ ${can_read} = 1 || ${can_list} = 1 ]]; 
        then
            echo "HTTP/1.1 503 Not Found";
            echo "Content-Type: text/html"
            for reply_header in "${REPLY_HEADERS[@]}"; do
                echo "${reply_header}"
            done
            printf "\r\n\r\n"
            echo "<title>503 Forbidden</title>";
            echo "<h3>I'm sorry, I'm afraid I can't let you see that</h3>";
            echo "<p>It seems that you tried to list a directory with a <code>.nolist</code> file in it, or a <code>.noread</code> file in it's parent, or a forbidden file type.</p>";
            echo "<p>If you think this was a mistake, I feel bad for you, son. I got 99 problems, but a 503 ain't one.</p>";
            log "503: ${request[@]}"
        else
            echo "HTTP/1.1 404 Not Found"
            echo "Content-Type: text/html"
            for reply_header in "${REPLY_HEADERS[@]}"; do
                echo "${reply_header}"
            done
            printf "\r\n\r\n"
            echo "<html><title>404</title><body>404, not found:<code>${request[1]}</code></body></html>"
            log "404: ${request[@]}"
        fi
        exit 0
    fi
}

# start socat on specified port
function start_server {
    echo "wtf.sh ${VERSION}, starting!";
    socat -T10 TCP-LISTEN:$2,fork,readbytes=4096,backlog=256,reuseaddr EXEC:"$1 -r" 9>&1
    echo "Socket was occupied... try again later...";
}

if [[ $# != 1 ]]
then
    echo "Usage: $0 port"
    exit
fi

if [[ $1 == '-r' ]]
then
    handle_connection
else
    start_server $0 $1 # start server on specified port
fi</span>