package main

import (
    "bufio"
    "fmt"
    "os"
    "time"
)

const (
    width  = 20
    height = 10
)

type point struct {
    x, y int
}

type snake struct {
    body []point
}

func main() {
    s := snake{
        body: []point{{width / 2, height / 2}},
    }

    fruit := point{3, 3}

    reader := bufio.NewReader(os.Stdin)

    for {
        clearScreen()
        draw(s, fruit)
        fmt.Print("Enter direction (w/a/s/d): ")
        direction, _ := reader.ReadString('\n')
        move(&s, direction[0])
    }
}

func clearScreen() {
    fmt.Print("\033[H\033[2J")
}

func draw(s snake, fruit point) {
    for y := 0; y < height; y++ {
        for x := 0; x < width; x++ {
            p := point{x, y}
            if contains(s.body, p) {
                fmt.Print("■")
            } else if p == fruit {
                fmt.Print("⚽")
            } else {
                fmt.Print(" ")
            }
        }
        fmt.Println()
    }
}

func move(s *snake, direction byte) {
    head := s.body[0]
    var newHead point

    switch direction {
    case 'w':
        newHead = point{head.x, head.y - 1}
    case 'a':
        newHead = point{head.x - 1, head.y}
    case 's':
        newHead = point{head.x, head.y + 1}
    case 'd':
        newHead = point{head.x + 1, head.y}
    }

    s.body = append([]point{newHead}, s.body...)
    time.Sleep(100 * time.Millisecond)
}

func contains(body []point, p point) bool {
    for _, b := range body {
        if b == p {
            return true
        }
    }
    return false
}
