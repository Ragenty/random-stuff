/*{ "fps": 10, "console": "asci", "min_c_version": 0 }*/
/*{
    "description": "A simple snake game in HolyC."
}*/

#define WIDTH 20
#define HEIGHT 10

typedef struct {
    int x, y;
} Point;

typedef struct {
    Point body[100];
    int length;
} Snake;

Point fruit;
Snake snake;

void setup() {
    snake.length = 1;
    snake.body[0].x = WIDTH / 2;
    snake.body[0].y = HEIGHT / 2;

    fruit.x = 3;
    fruit.y = 3;
}

void draw() {
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            int isSnake = 0;
            for (int i = 0; i < snake.length; i++) {
                if (snake.body[i].x == x && snake.body[i].y == y) {
                    isSnake = 1;
                    break;
                }
            }
            if (isSnake) {
                printf("X");
            } else if (fruit.x == x && fruit.y == y) {
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
}

int main() {
    setup();
    while (1) {
        draw();
        _sleep(1000);
    }
    return 0;
}
