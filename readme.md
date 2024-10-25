# HackingGame

You can start testing the game with

```shell
python HG
```

In the testing game, you have 4 programs in it.
One of them is the shell, named main. 

Other one is the "john". John communicates with the 
OS to do the port forwarding after a package cames 
to the PC by what the user is desired. Type john --help.

Other one is the "killer". Our serial killer does the
serial signal sending job. You can send anything with
it.

Other one is the network mapper. lol. NetworkMapper.
"nmap" so. this can scan the network. So lets test them
now.

## Testing

The thing you see when you start the project directly:

```shell
/#home:
```

Looks like a basic shell simulation.

Firstly, we need to listen the packages and see them.
Our shell have the ability to list the packages we have.
But for this, we need to forward our desired port to the
shell. For this, we can use "john".

```shell
/#home:john 1 main
```

This command will make a request to the OS to forward all
the port 1 packages to the "main" program, our shell. If
this operation is succesfull, "Connection succesful." is
the text we need to get.

After this, we can now listen all the packages from port 1,
we can hear the ping-pong packages. Yeah! I decided, port 1
should be the one that is being used by ping-pong packages.
Our network scanner program "nmap" uses this type of packages
too for scanning. Let's test.

```shell
/#home:nmap ping 192.168.1.2
```

192.168.1.2 is our ip address in this simulation. the program
"nmap" gets the command as a program argument. And then our
ip addresses to say all the computers that they needed to
send pong packages to us. If this command is succesfully
done too, we need to see a bunch of texts that saying we are
sending bunch of "ping" packages.

```shell
...
sending ping pkg to 192.168.1.39
sending ping pkg to 192.168.1.40
sending ping pkg to 192.168.1.41
sending ping pkg to 192.168.1.42
sending ping pkg to 192.168.1.43
sending ping pkg to 192.168.1.44
sending ping pkg to 192.168.1.45
sending ping pkg to 192.168.1.46
sending ping pkg to 192.168.1.47
sending ping pkg to 192.168.1.48
sending ping pkg to 192.168.1.49
sending ping pkg to 192.168.1.50
sending ping pkg to 192.168.1.51
sending ping pkg to 192.168.1.52
sending ping pkg to 192.168.1.53
sending ping pkg to 192.168.1.54
sending ping pkg to 192.168.1.55
sending ping pkg to 192.168.1.56
sending ping pkg to 192.168.1.57
sending ping pkg to 192.168.1.58
sending ping pkg to 192.168.1.59
sending ping pkg to 192.168.1.60
sending ping pkg to 192.168.1.61
sending ping pkg to 192.168.1.62
sending ping pkg to 192.168.1.63
sending ping pkg to 192.168.1.64
...
```

Now; let's check which computers ponged to us back.

```shell
/#home:main datas
```

With the "datas" argument, we can see the packages that being
forwarded to the "main" program. We should see something like

```shell
home : upcame connected datas:
        INTERNET:192.168.1.2:1:192.168.1.2
        INTERNET:192.168.1.2:1:192.168.1.5
```

this. This standard that I made out of gibberish, tells us,
two packages came to the ip address 192.168.1.2 from port 1
and one is from 192.168.1.2 (nmap sended that package to us
too) and one is from 192.168.1.5 (ping-pong packages contains
the ip address of the other computer for pinging and ponging
in this system). So 192.168.1.5 is an outsider.

So this is the kind of thing that could be done in this
simulation. Of course another programs could be adden to
the source code to make things more entertaining. In example
a SSH clone can be createn to simulate SSH hacking environment.
But thats not on educational purposes. And of course not on
practical purposes. What a purposeless machine.

You can do things outside of this paper in this ready simulation.
In example you can try to send a package to yourself with "killer"
and listen with "main". Let's see:

```shell
/#home:john 60 main
home : Connection succesful.

/#home:main datas
home : upcame connected datas:
        INTERNET:192.168.1.2:1:192.168.1.2
        INTERNET:192.168.1.2:1:192.168.1.5


/#home:killer
address:192.168.1.2
port:60
message:Hello world!
home : 
/#home:main datas
home : upcame connected datas:
        INTERNET:192.168.1.2:1:192.168.1.2
        INTERNET:192.168.1.2:1:192.168.1.5
        INTERNET:192.168.1.2:60:Hello world!


/#home:

```

When new programs are created, this thing can simulate
more fun things. In example, we could simulate hacking
google in it. Actually we are simulating. Take
a look at source code
