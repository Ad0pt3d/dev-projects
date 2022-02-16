"use strict";
// Port of the userdatas portion of the API
let lerp = (v1, v2, t) => {
    return v1 + (v2 - v1) * t;
};
class UDim {
    constructor(scale, offset) {
        this.Scale = scale;
        this.Offset = offset;
    }
    add(ud2) {
        let newScale = this.Scale + ud2.Scale;
        let newOffset = this.Offset + ud2.Offset;
        const newUDim = new UDim(newScale, newOffset);
        return newUDim;
    }
    minus(ud2) {
        let newScale = this.Scale - ud2.Scale;
        let newOffset = this.Offset - ud2.Offset;
        const newUDim = new UDim(newScale, newOffset);
        return newUDim;
    }
}
class UDim2 {
    constructor(x, y) {
        this.X = x;
        this.Y = y;
        this.Width = x;
        this.Height = y;
    }
    add(v2) {
        let x1 = this.X;
        let y1 = this.Y;
        let x2 = v2.X;
        let y2 = v2.Y;
        let nud = new UDim2(x1.add(x2), y1.add(y2));
        return nud;
    }
    minus(v2) {
        let x1 = this.X;
        let y1 = this.Y;
        let x2 = v2.X;
        let y2 = v2.Y;
        let nud = new UDim2(x1.minus(x2), y1.minus(y2));
        return nud;
    }
}
