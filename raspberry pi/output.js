var gpio = require('rpi-gpio');

module.exports = function () {
    return {

        off: function (pin) {
            gpio.setup(pin, function (err) {
                if (err)
                    throw err;
                gpio.write(pin, false, function (err) {
                    if (err)
                        throw err;
                })
            });
        },
        on: function (pin, dur) {
            gpio.setup(pin, function (err) {
                if (err)
                    throw err;
                gpio.write(pin, true, function (err) {
                    if (err)
                        throw err;
                });
                if (dur)
                    setTimeout(function () {
                        gpio.write(pin, false, function(err){
                            if (err)
                                throw err;
                        });
                    }, dur);

            });
        },
        destroy: gpio.destroy

    };
};