
class SquareCalculator {

    my_number = 0;

    set_input(some_number: number): void {
        this.my_number = some_number;
    }

    do_process(): void {
        this.my_number  = this.my_number * this.my_number; 
    }

    get_output(): number {
        return this.my_number;
    }
}

